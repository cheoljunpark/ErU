#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import pytesseract

# 이미지 파일 로드
image = cv2.imread('/home/ssafy/pp0258_1-19372.jpg')

if image is None:
    print("이미지를 로드할 수 없습니다.")
else:
    # 이미지 전처리를 위해 흑백으로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지에서 텍스트 추출
    text = pytesseract.image_to_string(gray, lang='eng')

    # 추출한 텍스트 출력
    print(text)