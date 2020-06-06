from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from urllib.parse import quote_plus
from urllib.parse import urlparse, parse_qs
from base64 import decodebytes, encodebytes
import json

class AliPay(object):
    """
    支付宝支付接口(PC端支付接口)
    """

    def __init__(self, appid, app_notify_url, app_private_key_path,
                 alipay_public_key_path, return_url, debug=False):
        self.appid = appid
        self.app_notify_url = app_notify_url
        self.app_private_key_path = app_private_key_path
        self.app_private_key = None
        self.return_url = return_url
        # self.app_private_key = RSA.importKey('-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAqOuBkd4Cqviq9eFJu74xTb/fiqN26DmTlaZgxOvZvWiY8PGG+DXeYCb6mbky7ufUS8DZcNfNgsfsSp+MQChJw1SywBpPhxbvmmgxs4q+1yDB7iyCTs06VToTQbNzGcieC//3bT6BeVXU4v6jsFR/+jwIgPAPhkNsNQQKy76WKz+1AHVPEgrLBbtQmojFCMaBR84Fk4amJii8gVsAXNvJMenYQdyamCHyNy94rZ6NXqrH2vdHwrv0oydd74NiFVg9oJqgoHY9RPzBjZUghWAssvB3Zq9sS/ZqWWbcAJUSOvLZW65CH5ba2SipaFYDvoMqlf0OVmJ6XzoSlMhqjs8WEQIDAQABAoIBAG20ffMBL9RgKZAE3PsM4YxXqyeDujhwc2FLQKn6Zjzyh9ihhuOyMIibK8MY9a4Vhi+hxEvhDwz4dE8HimZOTWF903DSjp4il3LP08PSKX1B55aCYfmswJarQ8vUNFyqERaUzUhAtWNalHrny4iPReYUUzOjwEjfety/M5awOZtggjHLDiNky/CNs8EKfFT5hPEQ75yj0QLMe540FVBhE/VB1XHirjXbUNymE5JQIo9MvOo9C26l4avvNonC/a7qpvdtHfEr8aGwQ5WvQZYpb1rcXwkEbfMu051Itw0NKJR6etUBLMlvxONJJv44XMN8/UyY+3mdqOv0xfj0AECgYEA9TQnp5Kw4RaAciO5ZPV5EzzQ3+mo6Rk/JkrjoIdalYJ5BYL703PsM4YxXqyeDujhwc2FLQKn6Zjzyh9ihhuO98W+lqFyFlxwudKtneGwrlSopNdD8S/HKCOWTwgYnH7bcqcJ39YNOYhde2+60Mc8bwBc3251i7eDqZmpa8xhxECgYEAsFuCQua9vo8KGqTyHL8WBHiyRM2e+RDkbY5tYNKI9kBq+T45MQ60gw5tzvZum4L8gxyP5z7TbgHBi10pVgeB7N5VHk9FptaqUMiqwkUWtnTVeNZrC8XAraA4HlQHKiZ5rHL9A+zjqj4l4VqBx2RuvHnG05lszqZ77PdrSRUanwECgYA0meKj3SEauEQHuEguM0as7M/2KN72WlcktM4OAttY1Wt21jmFjSqPD2jdWn0050bizWYNBbHoC6Ys44hpOnPEcUAxpreqWh3AbPOnHw8GuNDUVX6SQmepEXxYAkEEPWVtkRhclMHsXy3waXcaawRLi0RYbTEvlFBInkPI6UNbsQKBgHya22mroIsgg7IZsxtOhB76rHJimh0+qzchN/T+LFlZYHvkVAJucmpa6okdoz7riMCWkLKBuF90jCyM0WUAfvM+kAOPXRYpfEMB1WzX5dlaqW3GjqdUXzstod2PjXfTB7VvWW67CFdk83E7IsyUe+HV00wjSlhhhQDKOGFML8BAoGANZ4rsmUpViQt3LN3PTYO88uv3JZvpW8Hums2XgeSCsgo9M+u6vEu2tUbGMwl8CsW3s6TbO3TI1BWZkJlEx3FB+v66JNeOjBcW2MD8rogBMLIgmpKBtQ+3eRoVZBEAfm8e3JIkhVqiqBgKSsnu0t3b1DALiZp9OHXAedkPc6A8hc=\n-----END RSA PRIVATE KEY-----')
        # self.alipay_public_key = RSA.importKey('-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtXvlmFFzUpqA8QQ+C2R5gaD4UaYsFIIfXX5vnKaSUP+mXS8YSvr3jspNgjcJk1rWoIgXD2YeeexEurIYru0uYejCDSR1+dPg+uq2d3fV7FMWQmXt5gbqjIVFFBn0VlLeMexaf+bE39Schym8Vg1nXmbhePsG2DrA3odtwAvgdKlXYzYgSvdxuNJnUZeIGhrfo2uH+8xFw3G88G/4M8aV2RSVHpIBQUYUs+aNwFK6izHQXXpgI/I4B876zuelE2lsPOuvyCrdeUCD/JUEdX6qVoN41tm4y8dWQQubkKKD+bW/fB0iYUNCppJuG4HIlOT51E+KpHjL8/gCSea6GAf7wGjwkXGpwIDAQAB\n-----END PUBLIC KEY-----')
        with open(self.app_private_key_path) as fp:
            self.app_private_key = 'MIIEpAIBAAKCAQEApcoxpX0NzQ64hO0Qi8ZQLUETTkyrASSGA/BXGAmmVb/a/97lOxyrAX14T+emD97qFVLW9t8XJVxjFQzyhJ2N72ZL1cdtRnsf8++apQI60P2lNnhFcMXPuJW0ieNffnwbx4m8OdNSiD+WOIzjQM6EsQO+Uait7kfZ4P1/Wl2zqfv+X+XA0kE/VjgjUx/vdPDhK2mZ3PQXJ2uLwlD53+KfOwECl6Zrh/Jrsa3dicjooWiVXrvBvvRMwZG0YCdx4pbv/NBxVyKswCcSGnAPzzoBmk5YKX/EggvgL4jOVT919n+wwc30AAwaFNmyvr1WTA/zm3AKK7oqM4SyB3W4Te6PcwIDAQABAoIBAQCLVtG9HcqAorOwfLJgV4/BSSVZtJQwxKqiGtiISmvzO+lrDcIpmWGcQgDhX3cxdY/V1ib3m+6PJwPbiGM31FebcqWgChmsmAT191ZJAwO97MBzdEggjRCVObVgAqqa2uJaJUf+bb665n5yDu9c43WgdN37McLlNpxHPadQotpCrT8EQ5iCu4spCMB9tfqT94Z3M/fbZvYlfKs+UVBJPBZJ6j5RnfxtUH0f6qa6wdLFZ4JFEi/ozDRrdukVCkw9zW0xkI0T7cVZq13uct+6ycY7UzzwuuElmvc1Vis9NdyuYOG9uuf5nDyxXTAjL5YRp4Psj9k1Bk8Asq6S1YQNzGZBrF7wJvqm4EFMrsADKlnL/6fORBCj3wmO3Fa9CTD/zVrWiW6K4QFHHiN4doL2a5ekVfFBfSOT1LfL0deJ7lTxaqPYmArlA2fpPq5d8ECBTiS9ESKdUesJiQeRtNvw/KLBiiiC7nYBSlbYux5HVAOEzwLmAJ1DU6/KWlOG2MenauY0/fR30eClkFAoGBAM13eGLuuN+easOsCtNk8XZacJa/cQcgeltIBBy1msQ4cPNhV7YvQ0LvyXWaS/WI/Siwoztp0QYvJY7LSVQgkW14lJ5g51K5stuqtS2nhJOcYwArO+JveMOafjJB8Smp+8GZOIMVTo9FL2KZnuK3eDxoNTIxpluYmLwFpyi9o1Bk8Asq6S1YQNzGZBrF7wJvqm4EFMrsADKlzG1TRsxUcEnhMzsz+WYcnx3xuxUU+dhe3tB0XFICc2jSrmWYOBEU2F2mwwca4vBFNiXSLdCPE65ElHdY3L3/ctlHPcE8IE+JDefsUJ6/JzNuPV1uldp6gi46278mSS1flLAQPWkPMQ2veUU9AoGAc+fTR6v3Kl6JR7yDluC4vdUi8kcokaamn1Bk8Asq6S1YQNzGZBrF7wJvqm4EFMrsADK/OFGAzjVmv5tfyKdL/pN62DRPFXwSCo4LsEUFOpm//vMi/MoZpvy8mW3cqCs8yUkdrC0x0fKHSJr6aCPVKUATuz1YXGtEpv4PJFiewGJH+9mOiR0CgYAww54OuoGLTMncL+Q76IZsS4FcR8QZHd+0KQgFVhnBG1xmy0ueP1kGzy/cqNIMIUHzdt6gaQSkKvZ69D8kZUp/pvdX0Sqg0uQxoFgBV0H9rpW4SlDD6c1+c+kRj18bwawweTL/YizRu6dnHT4nGzv2zMd9uZZuK7DXj5boIzfV4w=='
        self.alipay_public_key_path = alipay_public_key_path
        with open(self.alipay_public_key_path) as fp:
            self.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtXvlmFFzUpqA8QQ+C2R5gaD4UaYsFIIfXX5vnKaSUP+mXS8YSvr3jspNgjcJk1rWoIgXD2YeeexEurIYru0uYejCDSR1+dPg+uq2d3fV7FMWQmXt5gbqjIVFFBn0VlLeMexaf+bE3LHa7rRk6Gh6DcbU6dfVHR1JQ3EkX3EEKQlXYzYgSvdxuNJnUZeIGhrfo2uH+8xFw3G88G/4M8aV2RSVHpIBQUYUs+aNwFK6izHQXXpgI/I4B876zuelE2lsPOuvyCrdeUCD/JUEdX6qVoN41tm4y8dWQQubkKKD+bW/fB0iYUNCppJuG4HIlOT51E+KpHjL8/gCSea6GAf7wGjwkXGpwIDAQAB'

        if debug is True:
            self.__gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.__gateway = "https://openapi.alipay.com/gateway.do"

    def direct_pay(self, subject, out_trade_no, total_amount, return_url=None, **kwargs):
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "FAST_INSTANT_TRADE_PAY",
            # "qr_pay_mode":4
        }

        biz_content.update(kwargs)
        data = self.build_body("alipay.trade.page.pay", biz_content, self.return_url)
        return self.sign_data(data)

    def build_body(self, method, biz_content, return_url=None):
        data = {
            "app_id": self.appid,
            "method": method,
            "charset": "utf-8",
            "sign_type": "RSA2",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0",
            "biz_content": biz_content
        }

        if return_url is not None:
            data["notify_url"] = self.app_notify_url
            data["return_url"] = self.return_url

        return data

    def sign_data(self, data):
        data.pop("sign", None)
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        unsigned_string = "&".join("{0}={1}".format(k, v) for k, v in unsigned_items)
        sign = self.sign(unsigned_string.encode("utf-8"))
        # ordered_items = self.ordered_data(data)
        quoted_string = "&".join("{0}={1}".format(k, quote_plus(v)) for k, v in unsigned_items)

        # 获得最终的订单信息字符串
        signed_string = quoted_string + "&sign=" + quote_plus(sign)
        return signed_string

    def ordered_data(self, data):
        complex_keys = []
        for key, value in data.items():
            if isinstance(value, dict):
                complex_keys.append(key)

        # 将字典类型的数据dump出来
        for key in complex_keys:
            data[key] = json.dumps(data[key], separators=(',', ':'))

        return sorted([(k, v) for k, v in data.items()])

    def sign(self, unsigned_string):
        # 开始计算签名
        key = self.app_private_key
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(SHA256.new(unsigned_string))
        # base64 编码，转换为unicode表示并移除回车
        sign = encodebytes(signature).decode("utf8").replace("\n", "")
        return sign

    def _verify(self, raw_content, signature):
        # 开始计算签名
        key = self.alipay_public_key
        signer = PKCS1_v1_5.new(key)
        digest = SHA256.new()
        digest.update(raw_content.encode("utf8"))
        if signer.verify(digest, decodebytes(signature.encode("utf8"))):
            return True
        return False

    def verify(self, data, signature):
        if "sign_type" in data:
            sign_type = data.pop("sign_type")
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        message = "&".join(u"{}={}".format(k, v) for k, v in unsigned_items)
        return self._verify(message, signature)
