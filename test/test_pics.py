from image_utils.converters.format_converter import FormatConverter

test_image_path = "../frontend/static/images/my_avatar.png"
output_path = "../../testfiles/out/imgs_output"
txt = "你好"

if __name__ == '__main__':
    converter = FormatConverter(test_image_path)
    converter.process(output_path, "png")