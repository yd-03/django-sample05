from django.db import models
import io
from PIL import Image


class UploadImage(models.Model):
    image = models.ImageField(upload_to="img/")
    result = models.ImageField(upload_to="result/")

    def transform(self, angle, gray):
        # 画像オブジェクトの生成
        org_image = Image.open(self.image)
        # 画像処理
        ret_img = org_image.rotate(angle)
        if gray:
            ret_img = ret_img.convert("L")
        # 画像処理後の画像をbufferに保存
        buffer = io.BytesIO()
        ret_img.save(fp=buffer, format=org_image.format)
        # 以前の画像を削除して新しい画像を保存
        self.result.delete()
        # bufferからのデータを保存
        self.result.save(name=self.image.name, content=buffer)
