#!/usr/bin/env python3
"""
Downloads Norway, Lumberjack, and Spruce cabin photos from Gmail
and files them into images/cabins/ with the correct structure.

HOW TO GET YOUR ACCESS TOKEN (takes ~30 seconds):
  1. Go to https://developers.google.com/oauthplayground/
  2. Click the gear icon (top right) → check "Use your own OAuth credentials"
     OR just leave defaults and continue
  3. In the left panel, scroll to "Gmail API v1" and select:
        https://www.googleapis.com/auth/gmail.readonly
  4. Click "Authorize APIs" → sign in with saykragness@gmail.com
  5. Click "Exchange authorization code for tokens"
  6. Copy the "Access token" value
  7. Paste it when this script prompts you  (token is valid ~1 hour)

Then run:  python3 download_cabin_photos.py
"""

import urllib.request
import urllib.error
import json
import base64
import os
import sys

# ── All attachment data (message_id, attachment_id, filename) ──────────────

ATTACHMENTS = {
    "norway": {
        "card": ("19ed09d3b9025bcc", "ANGjdJ_efdzX12X7gkDSuxloqL19yaox_FsgC7626Lhu5ZElAYNF4_cRP_w3RpVxuiVWY0_R8VLvl0-ZZE0Q0Dr4V09Fhj17-1qnS9AagaEhDmWAgGlxeRxv53WX235lLvoXjYVQ-CsBboYhVshwJrl9vC8k_txkccYg8Cu_EL94ALXlgQGBxRTl6CtjzuXOIXxJURafRvjSAQZWCr5hjqatlCUG_6Qz0DmGsVoSYbx-gVmyfsTkX02UoogE_Rim1gscN9JHFDHjS_wVzvM-LmrShftqb9rroSAVxVL4W9xyezZvvPcV0mqLsY0szdMwUA3yRRN1VKYLBlMv3swDmes82vv2W9rzC68cvWhQ7GVpdtKaKb0oOIen8l-gUg3IVYaIceguJcokNPzaL5oP"),
        "gallery": [
            ("19ed09d3b9025bcc", "ANGjdJ_4mzklo7xqduHonuadYKfCAj608pTeJZSWwfHSsK-muUzNhfZtLqAbuij7zvtXGNVuP3vb4ePwN0H1Z64f1-xkePWPRumwFE4hXQJvW7XTxp6xVq18Bxi5gnnxTCY0_LaJvzt04N1STqhPdFfvJyLH-ydFpBmkCJWWR6luqi83I5KS4GFtJ7knK7OYGhu34Jrc6zfWUNu60AHIEJWsTXMe8FFoZQ9c57Nfqm4ghReYdy-Jv3tna8dXLUagENyCJ0qsE3sF3FtMgfiO_XbIjhCp4k7pFs2fwiyDHk5a4fC8eJNouPm1qgEkdXDyui1CblMzzlOAozLGHSAx10ywrPBeo88SOPNMDNDXkchjJ1KZ04BqTOAN0C7l3BEXWisH_WX74LE5QR-2GlEQHwmZ0gHSF14Z1IBwVE3rfQ"),
            ("19ed09d3b9025bcc", "ANGjdJ_D5K93dU5nGybyShS6mlpRRgy4MgcpTWlpHISLQGmReuOiM3A-SwnpmW5njTrpTO3YwuMDV2_P26FyavkUjPKtOZ4APN5_eoJ1XYBX46puEItDhD9UXF2BnUPWaQkOj5YxmlqnZ5WwGxp1dUYRUgDGfClJAAmgSUVS0nxMTdKtc2gUy78aBJF9K57pJ5-MOIOHm3fuKKaV11z2fXrg20MUt87u73egVUORP6d6CX4DMW0iEr7B3Wb27l68_GjgaL8UinGb_HcN9nm-eKltopHY2S8PjQI-N3OPps7b8BimqEj7GJ7ypx-MrRSY8cOVYVsL-W6-ll-jNNUPuUEuMtxEiLc15i_CtvVZGZbTyOGvmWLjfK9MXr57tgQ13eaxl1-F3n8uE8ytLvnkw7eAooGA_ugOiBE5LnaIPw"),
            ("19ed09d3b9025bcc", "ANGjdJ_ucg0cERPNKDi1rs3IgmDYpsMTIMLFgfdew5d9g9C9mMAbpLDWhSIyY3kPP9fU5dydlK5X2O46DBEPsxQFkH14xQUurugWEH5_VOdWl1YCkBNGDpB1Cj88sE4IqcQSo390KMsffGrCD55TiLjOWLTPQS2tC4Q8aaPeu4asT5McAgyjLOvQ5LMg7mYewjQlC5rRbvNyzTtzRBky1bE43bVgWGPE7catZWNK4-qsF5WVP_7VeyZV82TK-sybgEmsjNUHfgEoGsstaTOXbqj78MAuh6ICxCW47IjFJb19DlTynO4Ynfc0lAhuHYGJ0yOgLWJS1j5AzXQoAa2uIohsoK63kbZUMJb6Foi2HCI6gVql9L5ylA0nzf9kmOKGzV2gyyWA7aKiUhQ-QaHX5ug2RjPecDtVUumOsOj54g"),
            ("19ed09d3b9025bcc", "ANGjdJ-qTh8AR9UW8XiBrexBDyG0m6xDQLE5l_Vg6mmftSdiKmOqBQj_OLKRBLCxGmur-PYEunoRGkTmrarsWJWoUGr2XAsMoOIbaDRmjZWEUy9CgVcd-rFq2At7k2WQP2hlZidOwuK0EFeI0dUAiS867I2yBoNKThyhROVgJMoANwSwFVbZkqq79mQP1lh1q306dcxw54IEc7-27ABvJHV65YSodGfZJY8OEj-9h2X9o8L7DnF46kKecL2V5xaO3aYl4CmVOZwmtuTAYDJJXYeOw137n1J3yyHwUT-5ru1_rU7Vde0cAc3wxhPyWjI8paOb7Qx_cATtl9LJUfzG-4xmL1t3o30Mb3wbBqZPeofNS4p1cBOLE0ydwr6nIWwyUCzT3pMC84irMumVF4_4qP5I-MR_DjlJWU8ye6ytqQ"),
            ("19ed09e70966e59b", "ANGjdJ9IWD9hl2WdlZCOpwGNhc_po0iDx0hsuHyHvTkDjh4fXq9gUedOsrOD5AfDXHceyU7QqCLFDBvG0tQc6PxjsNyG8j_lnJn5idZWwsuSS5zq_FhAQRcSQvGMkeq1bzEDvG5KL6htry_6nUQa1-wZELkPTaIGjbHG-wU2FPxtbjmZw8KzGV_a6W5Q2iQCT0dREoC6PlcIhJXi30d0Jj6v83hiQBRmkKYZ4Zt4gu5sPTLHNs8Mmgliy6Zw2M1lg_wPfFYHgoas5Qt8WtxkjtSSSdZ_GkLL4UtcJY-N83y3Q94SIlzl35IQ1Oe1rAdKbpvy1rh_WpCagDGkDGwXi9Lixa9EBtp_dW-S-i5ZPocxeymdIBoGFxw3wREE1-nSvRTZKoRuaOFY9kWMKfRo"),
            ("19ed09e70966e59b", "ANGjdJ8WyzCdKwlHAmit-SiQZrtDXh6vn6WTnjGVhnTuM1jxSUR9Sz1Fi6wud1CavsVCVl7WgMBG2pa_jVV9a_37GAgy7ObB0vK4P3QRRPUvGDt0zzeHFZGk8sKfvgBszups-yF7B7nNj0sRFoTfCZnORp9-BouIgtE8s2AWEqWEzMfhl2KufQ0A4kr9aAlXSScR_3Kji3dfPfvrDa83hVfIzzc4Tv6oJFFq9dhcVsXaoDtdFY4qNQ6bi7X2ScS51-Dpk1P4trHOWe2AXlrPiJkOuXMNjdB2Tul5dWDg0QhSV6VK8K0anV-CmlRTXNCQiRJhIaszPrwuBC4Y3DnGNcCrryoaC0Gbuu4S5Gw2136CiOSNX7O9kMwgpDT2f8LxcGEGlqhK-wK1D8FKRyImiu-CcJYcU6k0u2NcN9FjHw"),
            ("19ed09e70966e59b", "ANGjdJ_G5sVEJA9oTCcfzm02xmfvJ2A-dX53wOpKfXHcQAKmtngC9Tmcl4mKnTc8fhqNqaD2Q9ZdeyLP61NYqO1y4iwxGe14azZ_8Uaai14K1b6YM_fSFSEMWmsjiqjEEhGqfZVFh8TwjT9q446ZzBjcg-OcKjOHiugBDH7T-YEwsINwWUVr3ouoXZSlRrPVMf8-8Z0LVjQqhcJit3a-FHIHV91XHr7tx7NpwdcN978lzhwWBl_KWo3_4xhA5EMatrnb9sPwBBeRA04OEWwHca5du2T4adXnk8vuj1IyEeyjJzIBubau__x5c8HwK8iFq2ai_bobbqaN9eNsnCl0Nk7cq8oznuqI3SCgauv9IK65gA4PHkEV5-ZR3oexwaxUJGSHQjJ6m9Sz4gA4_pcPe3ChFd2ePO90v-TwvvwI8w"),
        ]
    },
    "spruce": {
        "card": ("19ed0a1abef9dae7", "ANGjdJ_fEiT1SI85KA-LdJLn7r132uajD1E0Xpj6UWQN51kWCW-nrsFyk9OJdrHYQ-o8iLv7FV2h-LjZ5x6to9AlGw43Ogyscw1RIpOVcmj5m5rr8ciUmGH4-bHRzWB9G0okOIkjhIby6HdmGiJIYedWK0emPcuAwhUCNt3FCQ2EPJxvXWEmkBgoEMf4o-EDYJlvBmgoByEAJkCE4IYxv6T8kEE-vzgr4ooQwzUBKxIjxsITAvVPA-lvdgMNRxGJqGm5_IDBsfFQCk_CmGitAsR-g2rjOws1fbIRlCA800r5L8JNnqXTWXFUSYLxE-jaJV90EDO4U1VW6hbaAZN_pI-9hYtqDUYto5oGrAyzQAkiAOVIoSSRNrcTthNrQ3WPLimF7I0bpLWu48HNmefv"),
        "gallery": [
            ("19ed0a1abef9dae7", "ANGjdJ-8jEcMF6zRCNyUgVO-Kf_sf-lHspP1qWnvgH0jBL5oVKNNj-FGgg06_muvyA_kz4hLPrhtSe2wvPm1-LyoUxHehz7NCG4QvwNsWgmS8PZx4afXQC1ZzHJCSq-tn2YaHitsJ_coZq_8luXRVnecGFWvi676a4Ro8n3Xrnk6WfViHQxsr5SPl_qz_eLWNOmtyMn4nRcoI4at8vJoJbm7c_L0Ikod7tEK9jS5RYGY_I9m0J4YWLrBreJ4kBkE-eumFcreQlzZNvL9aeq2uGEJ8t9FKYTINMe2ezpipMZWjPVX3_ZA8Lnd0JlEEW0OFHrvExg9_C91HbssWg4tAf6HUEdBxXRgTxGD9whAkvuPYm1eNOTFeZEq-7tXpLTuvufXpEvZ0PQ-Z5oClxkVU1khzSyv7tRHDvU3OixOMg"),
            ("19ed0a1abef9dae7", "ANGjdJ8rIhuwws23ud9_XeuKOy7UdNdCwOSqAjSIzYNUvVB83e91f2wccnP3to4w7MmIT91_PoOMfTJ_he8ceLXWyvsO2VXUseVv9ojARsfx35vx8xfUEwkkSq2D6tvrmkFJy2TPZa9uQACVQxaau9AUVHFvT5LNS8plj4VyVP4j8cmuuq2qFzyX9dqHMcpvoH2r6v94YMCZAF0NApb8QRvJHc4LBknwDySJVI9Yu26C5tX3CQr7Be3jQ9AgG_TOghAqlz4WkhE2oPh8vpx9pvfZ-cetQdjhDRK8_WjCmDo6JEIYwvPZyQ7aJxf_7e4b-KzTbFD2meU-r3paEpzgv7pCMaTLlEs_9QfJCO2V8mcuuyVZWf5dF1SyUhP3RMUAFfFH08BDBELjM5crNPYS7hAVv29YfB_Eta3TwVyGMg"),
            ("19ed0a1abef9dae7", "ANGjdJ8PqrnhN9KIxEi4dTPsYW68A1_L3W4rgcBLkAvYHfxaqcw4ZXtI5zRJsjftzRf6XYewtQQVXheVHyKVS4AVFzt1OWwmgxCPCIspekBVH5pymicYCstDlgEiuqTcGaDbAK1ZJQLZE3kYNZkzloHWEXVd4IKAid-pNQUYqgrVULPaon75aqg2emuIJ6Hez2J1Gozprnwz1DoOlst-Dv8v3zVwK1fWIn0Lz8_sAtmB4qKZqXIB_i1vrnlp70irxwDe2PwNwe3_yBxVtt4q0Bka4d9zqUNU4-ni28ORqOMwOc9s5CIjy5utWCTapbJpuToJI4CzMAghoHRifsr6ABCtlSiruF2ZPqaunIVEeIAIY2kNiSmwTo5iz54VworTERGvEWTgwSb5AAm5QfT5bk1DdOxOH1cm8Z8LeITQQQ"),
            ("19ed0a1abef9dae7", "ANGjdJ_OKNG17noHYHcRRxOONPUMPn08jRAm7jg0fdVTmkmhSROhqr0LwvLXhQeE5msktUerCdU3JJn-wmdh4uZs5rrc9iJR2cy7dlhNg5f4f6tdK_rq1i7j6Gwcy8vCBV44LXv6Blc7B7HejrKS4Mvyze5qARoZ1UbA0FikMkXpdRToROHMazhiJTpWkJik_pQbz5SGKwqLZ6QTe0aWNmXJhlfVSv4d4c_IB_UHs2Avfy5Bw_JJjahMjyU6UC_FRFQIQZqm1CxjocvDtQ1ZRaaFceQZsjon43JT1FdGiLBjlYRA5-msUw45YPcInyv2mcXtFr87YUoKwJ9i9N7LRy6KbylVmpW9gKoDQvXJxsz_Cev3uGu515pmOLIkkIQh9VmAQeU6P8fF3A8-F6Q6FnULz8OYMqflckzUq1DG_Q"),
        ]
    },
    "lumberjack": {
        "card": ("19ed0ae72d3f62fe", "ANGjdJ8DF886gnHlmpHYytLOweo4tvdbhL9nXvVngm_Z38WT5RZua61UobNNTTAGQWQn45OfiYAYH2TUfhcyPIGzHe2Xub7TKpnWGwjJWQFnDhcd8RORuX7IyZaQBE2l0KqZYfnrKxiPywXUlA1vdZb1rvtXSSi4o7y5GPq5kztiAQm9bXcUVAaTfiqr4j4vdeYcG91B_CSH3gUG_yheMBsKZRR6ispbU76_OPZ9ZMe49ziN1s2jlIhuwHmFFivMg9bQQDFyQb1epGfaqZ1UgXdOj3RIsNUR3CzsAEaCw3kF11wP5bYINm9RN6SHx8jd1jXtKO-O7xcPkrRx7dF_1BXZ03b6NG3_TKJ1Dq6K6QAPiWBCXfulTwHYWC5wFzB4QFqQn6wg6QUv6zsLeYXx"),
        "gallery": [
            ("19ed0ae72d3f62fe", "ANGjdJ8hyVfynnUqFY3mjbHauZbgKGOvlbyP32yJme03qfiSbp2qerRpXW03wSNI4RXWTwPrrYgTUryhL27LHmNd5FA8YUImC5VXKwShQ-F-R8En6gNG_pYL-BxQVa_HtQYxh2Sf6g05-zzMCTnISY7UiptuJf4h-Lk6MqfDTTDUR1Xi11fzI3rbeFPP3h_X5PYOZWt9DD_MqbuY_5cEhfxJapxnsmzTSSRh6-Q-rsytZJ0aqXrIyuWto4f94FDfX4S33u43iFAaZsy8qJMjvSDQX7awJ-pr3-MLGsg7dWdzJgahSjWsar8pCBHu5ud5h749ZNEhZ2jLNG6eVBD7COe-0vp46lpeqik8jKaCUc5A4AQ4nLefl6Z0RM0TKIDnKzjtdwjDmT9YkeYKHIU2cLMbONqnOPgWFdbPinvjGg"),
            ("19ed0ae72d3f62fe", "ANGjdJ--SsI3IiyWcT5NFGxZtnnmfY4pUC3442i6WEvnexW_8DpUH5y9YJuD3zcLNQhVXnqIjlOCz6RfJch1z8pB2I4s4JVLt5wsFhr8fMBVnz0HHnYFtL7Ifp_8aW7dhkV4CiSx-zT0bkq6pX82W3VOB4F-oxoK6hSfjnB0cXZQ0oOq1cM09DSjivtuyAiIM0VXwtTL6g7SBJ5cE7pb6uBiHfXSlOg_si2TtAJIzUaDlEReNmTSo4KHYxzYDlF-OuHpoONXomvwNrx7lO6foUd_1-7IXCSVYh4VW2it5f4ZaFCJoxiJPg2rcR0i3NM9Nixqkfo1fjOPUgZiFwS8-rq8civnautPV1C5MhSDdzF1g_rgq1hB9smXEYPwFj_Wlidp5cm9TYzPyH3-Jx-yeDlRnxlhDVl_VAanOTsm9A"),
            ("19ed0afee9dbf08e", "ANGjdJ9Dk_iSvOjEOY4gV8gpYtcIzFtiqFpuKLoTz8pTHLlfUvbp-z3Vexsp75Cg7q-UWcTBhj4vkbaac5E8_vXVcdBuuOyCnUgkhcB-9UpOo3jHd-SrEVay2A3o1rQBAScpkacs_sSQM82wrUwd2TzEfM6FJM86ezKMzr3URG_Jedr5xhHO9drltX6mAYyrHhjNF05ORD662AkPmQOiAS-K67IM_0_zvCsCW0Qz2vWSP5n_FT4TxF88e2CV-21qJPF7VAmdt2O9OhkXA--dtsl2OtpAoczAeL-mHLpNiuILnPwPW8Sxb3xfqXT3FMbEiF7ro6WBP8_L87AUz8_HH_RIsQzDDLidXlldUY9hRMhSwgC_iqec0bYRBiIg1NbnF5wH85yeY1xcKCcSDfOu"),
            ("19ed0afee9dbf08e", "ANGjdJ_YWzEBxb-QZBCmQijk1T8u2Ve0VQ7T7wHaRRpIIhXZWyLLix4IG5QFZ2ZBZ5sYxr3Amqm3SLh208UwqY5LIWN_UTirnuS0YkaU6elYBxuimVeANIyE6XusTe-0GQtqkXWc0vCVnG-qzeAubVkA9ODZmsRI9O2clrTfls5Ft_PLSzp4iNx9ndMRhzAtZ4dW1g-Ood4-WQ8GUA5VTn2ceJenSHFN-85KKf4KysIRrlgP89T2yrnnmy9jS3HuTzO_7ZjtluKzffo5DryyQa-2WAq6LmY9Pap2lF5FQ8LaceAXdU-9mUl1guxGq0h1sPBrEK1S-K685nhhzSSj1wk7MjCTEBStXoX_V7V5HIMOnOB_84bG-y9gjbJLBtbieo-Jc33QghyHYVeaRGONib_JgzNfy3UCR504YsTqlQ"),
            ("19ed0b1161e00915", "ANGjdJ95TICbS1sh0jQvWkJLBlN5KAVTFbjNO_fPHUEx3Ro1cZPBN_Co1Fij73JEpet1FqJHKH3nanJlwBaeGeWKirRmt2SxE5gWJHke3itRFEYNVqhgvGwm1jCUh3rVpzX8WxqGG8_VCkZk56zDGB4Ca4QUL3shhdPsM-NfYRd7jAIu1VDGpw87FE51jkLvQJxU9lMGa0wEdAljXOBwT1LqXapeg6NGLEdIsGWxhnt2e5V6YmWO11LIBQu6Vpc4vZO2dag0fnF3apCXjaZeye-7ebxlYEbyVa3WZuSFDR7lg9Vpp5WIsD6vz5rrDBI3jU_thaRPlOl9MVClrwKKjT_BNKrtYQfldhdCGVCLU0iz8ZcfelbXrRMqdsxznoZfV_lwZgU04RxD07OD9QPz"),
            ("19ed0b1161e00915", "ANGjdJ_4doImdX7X91JgWewrUeRaw9P9FlfmNgCSj_22HIAD40r6IIbvnTiCt6GNqLj-A5w2fjWJR0N5JPnKEwD6PRDJNIYWllvNl8qYcLpJ0GNB9xUBck7NsuOvcznFhVNPMFwkIx58OrE7m2l7JJHMYYg9SuCvEVlsVPTp5aLKSLytRRDodtJzFIBb-o5C0WAbuvWxlhd1N1IB8Qabz7tBcsQq3W07BozIMC86ufMcnkSYIPWp2Wnrh5sw3DgUB1FYf8Xu_Tz5IfGMRncXmS7DyagFN1L2SpjIQaaKaPqeRzzAFz1YvuR17_mkSZkXsGt16gWOPQRENXCb8H9_tdfqOCz4gzT3Q24eZMNUgGnk6XbThBYO-DCwI7e8q3pXuP9pE8TjPi-ELl4jH4w7hI3ZqEJmagepvcw6tS-7hw"),
            ("19ed0b2f9d2af3db", "ANGjdJ_tftn4W630IIiDrfFwrgfgKgKdB90SSFuw2bR_UOtg97jvfzcChllX-O8zBmvr-fseJsnJI-brlmwJyGSJ5sHIUXUqkTrXZtMCFu07RX5hHUdWQSTLW_kN8GgWUqKu-9A6HQkkM4HMFtIaFrErk47TWAfRj6lidB7Je1ZRZO5UQTYq_4FMXA0ToIJ4ABMJEv0B4iInXRDx5QWxSVLcrZ8FDhDVOiJKrPcY-Y0sOv4INEsZyB2z2ujl28FLZRntSSKSIz8ebWEdZO6NbowRBeECb37rf7DedfG1dR78pQYFkk0CBLQG3b9w62EEdXdUCEJoR1wKuUqd2b4YRH0-KHvvFs82v5PUdw5Nh0R-ekl5ZLCgcI900DYoUPM3DTltCeTbGNq6_XfTYj2e"),
        ]
    }
}


def fetch_attachment(token, message_id, attachment_id):
    url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}/attachments/{attachment_id}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    # Gmail uses URL-safe base64 with padding omitted
    raw = data["data"].replace("-", "+").replace("_", "/")
    padding = 4 - len(raw) % 4
    if padding != 4:
        raw += "=" * padding
    return base64.b64decode(raw)


def main():
    print(__doc__)
    token = input("Paste access token: ").strip()
    if not token:
        sys.exit("No token provided.")

    base = os.path.expanduser("~/Desktop/NEW Muskego/images/cabins")

    for cabin, data in ATTACHMENTS.items():
        print(f"\n── {cabin.upper()} ──")
        gallery_dir = os.path.join(base, cabin)
        os.makedirs(gallery_dir, exist_ok=True)

        # Card image
        msg_id, att_id = data["card"]
        print(f"  Downloading card image...", end=" ", flush=True)
        img_bytes = fetch_attachment(token, msg_id, att_id)
        card_path = os.path.join(base, f"{cabin}.jpeg")
        with open(card_path, "wb") as f:
            f.write(img_bytes)
        print(f"✓  →  images/cabins/{cabin}.jpeg  ({len(img_bytes)//1024}KB)")

        # Gallery images
        for i, (msg_id, att_id) in enumerate(data["gallery"], start=1):
            print(f"  Downloading gallery {i}/{len(data['gallery'])}...", end=" ", flush=True)
            img_bytes = fetch_attachment(token, msg_id, att_id)
            path = os.path.join(gallery_dir, f"{i}.jpeg")
            with open(path, "wb") as f:
                f.write(img_bytes)
            print(f"✓  →  images/cabins/{cabin}/{i}.jpeg  ({len(img_bytes)//1024}KB)")

    print("\n✅  All done!")


if __name__ == "__main__":
    main()
