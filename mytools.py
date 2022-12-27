import json
import time

import requests
import uuid

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhMzA1OTg2MDQ1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJnZW9pcF9jb3VudHJ5IjoiVVMifSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InVzZXJfaWQiOiJ1c2VyLVIxT2ZueE5JMFk4R05HZTE4bU1ZOWhwMiJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiYXV0aDB8NjM5MTVkYjg4ZjJmOWQ4MzEzZmE5NTZjIiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjcwNDcxNzg0LCJleHAiOjE2NzA1NTgxODQsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb2ZmbGluZV9hY2Nlc3MifQ.UlTPnpSbLHeS4mqdzCNy_jBmexalt1z5lik3eK0Ui4XCgFMvY5ohcK_FRnz_uthoiqLAt7Il3fukLwIF8UeYpU_fOHLnvY8MncdbpX_T08l8_qC06sWGcqWQfsADPGiRCHjNXfX1_CmyK5FGlQkpuFImc6bfGh6dP8z63PwFxm1XKjpRtmSB5xe9RdTqJXkLtQprOQgXenfBumnj6136m4UE34koOizACgxVPaLfI5IoC7PRRIiYYKvfvj1k9huF2diaqApexnwmIjFZeaOh-B-8N2P-V4RtGdiWlJ74TeQAk9KuAlVveTKdyeFaJWNunGkbWoHs6Wq09FuJ0-Humw",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Cookie": "_ga=GA1.2.1013169743.1670424670; _gid=GA1.2.1478695020.1670424670; intercom-session-dgkjq2bp=UHVReTI5N1VIL1pkMFdiVmRwd3RZcGRMRDJ0QVZpMTdJcTIvRnVhaEZRSlZtVUcyVmhnUzhtdWJxR2ExTUVTaS0tNXU1SUFQekE5NExhd3RrWHNDbktXdz09--d7fe5bef679ea6cc13cfbde33d211bf04b742e36; intercom-device-id-dgkjq2bp=b91764c6-0e54-4e64-9fc1-212acb83e687; __Host-next-auth.csrf-token=842bb5fe16f319eb9e8c1bded535b08072dc6e4aa0744ada34fb6d08c9589651%7Cfbde89c1a73d6778da871db921fab0aa610a885b53a9218a2719a2618ad5fca4; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com%2F; mp_d7d7628de9d5e6160010b84db960a7ee_mixpanel=%7B%22distinct_id%22%3A%20%22user-R1OfnxNI0Y8GNGe18mMY9hp2%22%2C%22%24device_id%22%3A%20%22184efd621e2cd-0366ca768754ff-26021151-144000-184efd621e3a5%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%22user-R1OfnxNI0Y8GNGe18mMY9hp2%22%7D; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..yYGqsMbxTXg-rV_S.qfWWK8TaaXn2peygusIc0V9345_PWRKAWDNPH7JNJ9N9nWYB3DcNCM6SCPPSPvGBi4aFqp1COnkOpbQzRu5s4uWpjhZ0Z4qf4mJtMWkQMr6o3Q5OdDcU2-UKGYUJ10zkLeZ7Sf8WxsIL-f6m5XmuEadLvtP2xNP13Mf2TWU4yOfaQ7KfFQ61wuh_laKcROq1v5ynmXiq0DDh4P3L9s-NpOO9lkhJMkI69nFTZiehDeAJRCDtPhRWc6i0LLpWngUCibY5Xxq1z1a25hWAT6jeXgXVw2m3g6D89jrfBJ9486uYrTpE2cu_59CGz8BYRFiDgBpgz3u1UAMIwklhMWQ0vLWqZJVUCJWe_hsQzS4yM8qFKAEQS6y_z6mpkIwUJWpi9wLIXAOzL1cqvYU2iv34aoiBz-kZhBHPx8z1zW2o2XoFOLjgbLJHM-O66G1YEeQRnAVLVual2PUOdoQJMoNdfKQd9yD9r-Rv5a4Yvo7YxFWs_PtIm2gj2tkYWRRQD5TjRtdLXVGFeV9tDTcTG-ib5tZSO3xZaBnKA4jUbeKuNOyXnvldCWjGlNYwFq_I2foEfTC-bvAhIs44MqSylecK9kLp9B3Z1GPq7EoqKMnI_iM-gJulXHya5A4pleNSGxUoMlbs_AK9JdaLqo-RaV-Vg4cFxTNsJeSkAH7WZV6cTNoO2RjmPtjV74IoqkMeUiDPLQzB3uULrC_BgDw5OgTz8JFPtdOyi0gvd0aCMInSLopH7RZnsUdRN7UPeD9wolBrSPhYZk6IKUSuBfLq9Ik7tp9FcmHNYP16FI2P808fjr5S-Gl1sp_AtgAY7LTvM_cGKdr8Kk9cf3ngLyFg53vxlJjXwPXAll2hHMetaqn2gbQKc-zn1QYl7YvznjS4xNcW65Uc9MOJiPqMNiFtsS6ZsntK3cHow_ePLXBGaVLlWTQ0q78cSfUvfj0HtYdpDWL2kxQf1WtRVm0WTmv9SiJRddaz9EjEcylT_9_Vk_N43CJYD5ZdgwnLxXBU9JAJOza0WdJvjHjlbug4P4wxYWX7BNaIJFtLHkUyqG-2jDwQZp8dErH6O4uwg0V8axbJrbXho7pCt2Hx4uTlKXsc5U5lHJxuOzQPcs5io6vuTmHYH-HO0a9xtO2mxmN97y1JRirOFVpV6WD-eZEheNMGKe1kDLS7ZM2KMsDW3Zu11Hii6Jl_R2qmwzaPuNb6xHwjohA1aHgrzS_EZ83_O-eCFt-1eMQgarRideb8iiDuK5kSpzoVxp1E9qXEF8fVHb7TiZi5CMldr8MqWMkCDAxo2PRU2Y6DRoOnAjsAKVybtcQpYGzlk90SKI0T_6hn1QoQx4Hsv7eDCyjvy8_vQgMCXUf7b6zAVEFarPEyLpi-tWd_4wRcUUUVSDS93a0La-hIMWb8bugUlslLJnADc9c9Sww4uty8fDFJRLVIiBIHdXE3mjisi_cTUGk1Ah3fu1JvTLHWpkyyF0LtPweFYPRrn_mBSXHRsBACaa18sSNr-TPtaXLThIvKdIrvpzBw07xfVuHIdZ4HNmwJeKNyjOlzZvpo3QcPUMUjyAw7aRAeR_NBRepAl9enG8-JcC0acYJPM3Co1e5ttrzxmxRe7smhHTq38MmiyUwdq4_ku5c86l1TGV20vBZ_GMDqudU70EwDQMGbyziFHTncvNXc14av9gHqfI3UsZdr-VF4m_Yo8WnKRkwA9PIXsWWpCHimbqSancsNclmBiZrfZ2fyPbjOIJTS5OP9STAQKufK9pj6SkWVAOlAkFVbipp_Atwt51zEbJBZm2xESSI3rA6VDc1N5RenTKRLg3xo_rjj5JTDhFAn7HA-6DpAnHPWfKD-QWoHK3Ry-O0Wnh7RhZ9uYCTR4VXhwqRBTi5vuKID0BwLUbQ5sPM6yes4wes1XV_QQh-9WhdNMAtmtDPszNhoqKRfMkSSQ5Es1gogPKJxEoeULyU2xqZs82FYX-g0w2n1yAyAq4A2yF10svgyPX_UviiVlCEhdFTXlJq-N6RYnNK1MA3Ui0LJIF-aNY2geJwOZBhy3a1NCItmSV8dUyv7sld6xVRcYAY_BWvaTh1u0ZWOiGxSho7m1brvV1IgAXpMD9YR8m_TGK59q-VVXx2t07OMQBXXR4v1pZVvkfZoer5_B11x0t0ztqikn5Fe_sgQxgyC2ZJiCOkIxGkM3a5qyXBVtgsScWIog2Yb1CAtDQTKObVWSuwlG3J0HFYG0UEIilEBg1mPaHdUX8ZkWhiVWuGcAurCS4_SWJjVlj9wEwuJ-Mnx7gXhh1N-upOYPOvMqNTc4b0HmbYXCvh0y_KZ5r-Iwamchx4DokM004XH5tcbA3BPTdlEz8o.OGJyYEw41_05nyouzf2lVQ"
}
body = {
    "action": "next",
    "messages": [
        {
            "id": "",
            "role": "user",
            "content": {
                "content_type": "text",
                "parts": [
                    ""
                ]
            }
        }
    ],
    "parent_message_id": "",
    "model": "text-davinci-002-render"
}

conversation_id = ""
parent_message_id = ""


def get_chatgpt_once_api(search):
    global conversation_id, parent_message_id
    # 如果上一条消息id为空 则随机创建一条
    if parent_message_id == "":
        parent_message_id = str(uuid.uuid4())

    # 消息主题id为空则不附带消息主题id
    if conversation_id != "":
        body["conversation_id"] = conversation_id
    body["messages"][0]["content"]["parts"][0] = search
    body["messages"][0]["id"] = str(uuid.uuid4())
    body["parent_message_id"] = parent_message_id

    response = requests.post("https://chat.openai.com/backend-api/conversation", json=body, headers=headers)
    if response.status_code != 200:
        return "出现错误 请重试!" + response.text

    datas = json.loads(response.text.splitlines()[-4][6:])
    parent_message_id = datas["message"]["id"]
    conversation_id = datas["conversation_id"]
    return datas["message"]["content"]["parts"][0]

