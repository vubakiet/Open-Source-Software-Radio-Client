# from PIL import Image, ImageDraw
# import math

# # Đường dẫn đến file ảnh
# input_path = r"D:\\SGU\\Opensource_Software\\radio-client\\assets\\wangjunkai.jpg"

# # Đọc ảnh vào đối tượng Image
# img = Image.open(input_path)

# # Tính kích thước ảnh và bán kính
# width, height = img.size
# radius = min(width, height) // 2

# # Tạo ảnh trống để chứa ảnh sau khi xoay
# new_img = Image.new("RGBA", (radius * 2, radius * 2), (0, 0, 0, 0))

# # Lấy đối tượng vẽ của ảnh mới
# draw = ImageDraw.Draw(new_img)

# # Vòng lặp để xoay ảnh và vẽ lên ảnh mới
# angle = 0
# while True:
#     # Tạo ảnh mới theo góc độ hiện tại
#     rotated_img = img.rotate(angle)

#     # Tính toạ độ để vẽ ảnh lên ảnh mới
#     x = radius - rotated_img.width // 2
#     y = radius - rotated_img.height // 2

#     # Vẽ ảnh lên ảnh mới
#     new_img.paste(rotated_img, (x, y), rotated_img)

#     # Vẽ một hình tròn để làm border cho ảnh
#     draw.ellipse((0, 0, new_img.width, new_img.height),
#                  outline="white", width=10)

#     # Hiển thị ảnh
#     new_img.show()

#     # Tăng góc độ lên một lượng nhỏ
#     angle += 5

#     # Nếu góc độ vượt quá 360 độ thì quay trở lại 0 độ
#     if angle >= 360:
#         angle = 0


# from tkinter import *
# from urllib.request import urlopen
# from PIL import ImageTk, Image
# from io import BytesIO

# # Tạo cửa sổ chính
# root = Tk()

# url = "https://scontent.fsgn2-7.fna.fbcdn.net/v/t1.6435-9/110317078_108873884247194_8632694263271216467_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=CYkmKjjJ3K8AX8vLrAb&_nc_ht=scontent.fsgn2-7.fna&oh=00_AfBiwiyFddEmezj0zF8kj61iY3RTbmJluODDF6b12I6c5A&oe=6476F918"
# image_bytes = urlopen(url).read()

# image = Image.open(BytesIO(image_bytes))
# img_width, img_height = image.size

# # Tính đường kính của hình tròn
# diameter = min(img_width, img_height)

# # Crop hình ảnh thành hình tròn
# img = image.crop((0, 0, diameter, diameter))
# img = img.resize((300, 300))

# photo = ImageTk.PhotoImage(img)

# label = Label(root, image=photo)
# label.pack()

# root.mainloop()
