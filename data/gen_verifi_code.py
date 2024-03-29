from captcha.image import ImageCaptcha
import random
import tqdm
import numpy as np
import string
import cv2
import os

# characters = string.digits + string.ascii_uppercase
characters = string.digits
out_root = "../data/verifi-code"
if not os.path.exists(out_root):
    os.makedirs(out_root)

width, height, n_len, n_class = 170, 80, 4, len(characters)

generator = ImageCaptcha(width=width, height=height, fonts=['fonts/arial.ttf',
                                                            'fonts/calibrili.ttf',
                                                            'fonts/songti.ttf',
                                                            'fonts/cambriai.ttf',
                                                            'fonts/consola.ttf',
                                                            'fonts/consolab.ttf',
                                                            'fonts/corbel.ttf',
                                                            'fonts/HarmonyOS_Sans_SC_Regular.ttf',
                                                            'fonts/simfang.ttf',
                                                            'fonts/simhei.ttf'])

for i in tqdm.tqdm(range(50000)):
    random_str = ''.join([random.choice(characters) for j in range(4)])
    img = generator.generate_image(random_str)

    im = np.array(img)[:, :, ::-1]

    cv2.imwrite(os.path.join(out_root, random_str + "_" +
                str(random.randint(0, 9999)) + ".jpg"), im)
