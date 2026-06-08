/* Muskego Point Resort — Shared JS */

(function () {
  'use strict';

  /* ---- Nav: scrolled state ---- */
  const nav = document.querySelector('.site-nav');
  if (nav) {
    const onScroll = () => {
      nav.classList.toggle('scrolled', window.scrollY > 24);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- Nav: hamburger toggle ---- */
  const hamburger = document.querySelector('.nav-hamburger');
  const mobileNav = document.querySelector('.nav-mobile');
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      const expanded = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', String(!expanded));
      mobileNav.classList.toggle('open', !expanded);
    });

    /* Close mobile nav when a link is clicked */
    mobileNav.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileNav.classList.remove('open');
      });
    });

    /* Close on click outside */
    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target)) {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileNav.classList.remove('open');
      }
    });
  }

  /* ---- Scroll-reveal ---- */
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const delay = entry.target.dataset.delay || 0;
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, Number(delay));
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(el => observer.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('visible'));
  }

  /* ---- Cabin gallery: thumbnail switcher ---- */
  const galleryHero = document.querySelector('.cabin-gallery-hero img');
  const thumbEls = document.querySelectorAll('.cabin-gallery-thumb');
  if (galleryHero && thumbEls.length) {
    thumbEls.forEach((thumb) => {
      thumb.addEventListener('click', () => {
        const img = thumb.querySelector('img');
        galleryHero.src = img.src;
        galleryHero.alt = img.alt;
        thumbEls.forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');
      });
    });
    if (thumbEls[0]) thumbEls[0].classList.add('active');
  }

  /* ---- Lightbox ---- */
  (function () {
    const gallery = document.querySelector('.cabin-gallery');
    if (!gallery) return;

    const thumbs = Array.from(gallery.querySelectorAll('.cabin-gallery-thumb'));
    if (!thumbs.length) return;

    const images = thumbs.map(t => {
      const img = t.querySelector('img');
      return { src: img.src, alt: img.alt || '' };
    });

    let currentIndex = 0;
    let lb = null, lbImg = null, lbCounter = null;

    function build() {
      lb = document.createElement('div');
      lb.className = 'lightbox';
      lb.setAttribute('role', 'dialog');
      lb.setAttribute('aria-modal', 'true');
      lb.setAttribute('aria-label', 'Photo viewer');
      if (images.length === 1) lb.setAttribute('data-single', '');

      const wrap = document.createElement('div');
      wrap.className = 'lightbox-img-wrap';

      lbImg = document.createElement('img');
      lbImg.className = 'lightbox-img';
      wrap.appendChild(lbImg);
      lb.appendChild(wrap);

      const closeBtn = makeBtn('lightbox-close', 'Close', '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>');
      const prevBtn  = makeBtn('lightbox-prev',  'Previous photo', '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/></svg>');
      const nextBtn  = makeBtn('lightbox-next',  'Next photo',     '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg>');

      lbCounter = document.createElement('p');
      lbCounter.className = 'lightbox-counter';

      lb.appendChild(closeBtn);
      lb.appendChild(prevBtn);
      lb.appendChild(nextBtn);
      lb.appendChild(lbCounter);
      document.body.appendChild(lb);

      closeBtn.addEventListener('click', close);
      prevBtn.addEventListener('click',  () => navigate(-1));
      nextBtn.addEventListener('click',  () => navigate(1));

      lb.addEventListener('click', (e) => {
        if (e.target === lb || e.target === wrap) close();
      });
    }

    function makeBtn(cls, label, svg) {
      const btn = document.createElement('button');
      btn.className = cls;
      btn.setAttribute('aria-label', label);
      btn.innerHTML = svg;
      return btn;
    }

    function show(index) {
      const { src, alt } = images[index];
      lbImg.classList.add('swapping');
      lbImg.onload = () => lbImg.classList.remove('swapping');
      lbImg.src = src;
      lbImg.alt = alt;
      lbCounter.textContent = (index + 1) + ' / ' + images.length;
      thumbs.forEach((t, i) => t.classList.toggle('active', i === index));
      if (galleryHero) { galleryHero.src = src; galleryHero.alt = alt; }
    }

    function open(index) {
      currentIndex = index;
      if (!lb) build();
      show(currentIndex);
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.lightbox-close').focus();
    }

    function close() {
      if (!lb) return;
      lb.classList.remove('open');
      document.body.style.overflow = '';
    }

    function navigate(dir) {
      currentIndex = (currentIndex + dir + images.length) % images.length;
      show(currentIndex);
    }

    document.addEventListener('keydown', (e) => {
      if (!lb || !lb.classList.contains('open')) return;
      if (e.key === 'Escape')     { e.preventDefault(); close(); }
      if (e.key === 'ArrowLeft')  { e.preventDefault(); navigate(-1); }
      if (e.key === 'ArrowRight') { e.preventDefault(); navigate(1); }
    });

    /* Hero click → open at current active thumb */
    const heroWrap = gallery.querySelector('.cabin-gallery-hero');
    if (heroWrap) {
      heroWrap.addEventListener('click', () => {
        const active = thumbs.findIndex(t => t.classList.contains('active'));
        open(active >= 0 ? active : 0);
      });
    }

    /* Thumb click → open lightbox (hero swap handled by existing switcher above) */
    thumbs.forEach((thumb, i) => {
      thumb.addEventListener('click', () => open(i));
    });
  }());

  /* ---- Gallery: drag to scroll ---- */
  const galleryTrack = document.querySelector('.gallery-scroll-track');
  if (galleryTrack) {
    let isDown = false, startX, scrollLeft;
    galleryTrack.addEventListener('mousedown', (e) => {
      isDown = true;
      galleryTrack.classList.add('grabbing');
      startX = e.pageX - galleryTrack.offsetLeft;
      scrollLeft = galleryTrack.scrollLeft;
    });
    galleryTrack.addEventListener('mouseleave', () => { isDown = false; galleryTrack.classList.remove('grabbing'); });
    galleryTrack.addEventListener('mouseup', () => { isDown = false; galleryTrack.classList.remove('grabbing'); });
    galleryTrack.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - galleryTrack.offsetLeft;
      galleryTrack.scrollLeft = scrollLeft - (x - startX) * 1.4;
    });
  }

  /* Fallback: force any remaining reveals visible after 1s (catches headless screenshots) */
  setTimeout(() => {
    document.querySelectorAll('.reveal:not(.visible)').forEach(el => el.classList.add('visible'));
  }, 1000);

  /* ---- Mark current nav link as active ---- */
  const currentPath = window.location.pathname.replace(/\/$/, '') || '/index.html';
  document.querySelectorAll('.nav-link, .nav-mobile .nav-link').forEach(link => {
    const href = link.getAttribute('href') || '';
    const linkPath = href.replace(/\/$/, '') || '/index.html';
    if (currentPath === linkPath ||
        (currentPath === '' && linkPath === '/index.html') ||
        (currentPath.endsWith('index.html') && linkPath === '/index.html')) {
      link.classList.add('active');
    }
  });

})();
