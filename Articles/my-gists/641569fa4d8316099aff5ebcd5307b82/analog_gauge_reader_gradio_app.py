import os
import cv2
import time
import zipfile
import tempfile
import random
import json
import yaml
import toml
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import gradio as gr

class Interface:

    def upload_file(files):
        file_paths = [file.name for file in files]
        if file_paths:
            return file_paths[0], file_paths
        else:
            return None, []

    def get_tempdir():
        timestamp = int(time.time())
        temp_dir = tempfile.mkdtemp()
        return timestamp, temp_dir

    def create_zip(zip_path, filelist):
        if not filelist:
            return
        else:
            with zipfile.ZipFile(zip_path, "w") as zipf:
                for file in filelist:
                    zipf.write(file, os.path.basename(file))
            return zip_path


def add_():
    pass

def remove_():
    pass

def show_rectangle(images, x, y, w, h):
    rect_images_path = []
    for img in images:
        image = cv2.imread(img.name)
        overlay = image.copy()
        cv2.rectangle(overlay, (x, y), (x + w, y + h), (128, 128, 128), -1)
        alpha = 0.5
        image_with_rect = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
        cv2.imwrite(img.name, image_with_rect)
        rect_images_path.append(img.name)
    return gr.Image.update(cv2.imread(rect_images_path[0])), gr.Files.update(rect_images_path)

def resize(images, scale):
    resized_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        resized_image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
        cv2.imwrite(img.name, resized_image)
        resized_images_path.append(img.name)
    return gr.Image.update(cv2.imread(resized_images_path[0])), gr.Files.update(resized_images_path)

def crop(images, x, y, w, h):
    cropped_images = []
    cropped_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        cropped = image[y:y+h, x:x+w]
        cv2.imwrite(img.name, cropped)

        cropped_images.append(cropped)
        cropped_images_path.append(img.name)
    return gr.Image.update(cropped_images[0]), gr.Files.update(cropped_images_path)

def squiz(images, fx=0.5, fy=0.5):
    squizzed_images = []
    squizzed_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        resized = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)
        cv2.imwrite(img.name, resized)
        squizzed_images.append(resized)
        squizzed_images_path.append(img.name)
    return gr.Image.update(squizzed_images[0]), gr.Files.update(squizzed_images_path)

def mask(images, mask_file):
    masked_images_path = []
    mask = cv2.imread(mask_file.name, cv2.IMREAD_GRAYSCALE)
    for img in images:
        image = cv2.imread(img.name)
        masked_image = cv2.bitwise_and(image, image, mask=mask)
        cv2.imwrite(img.name, masked_image)
        masked_images_path.append(img.name)
    return gr.Image.update(cv2.imread(masked_images_path[0])), gr.Files.update(masked_images_path)

def binarize(images):
    binary_images = []
    binary_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        if len(image.shape) == 3:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray_image = image
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        cv2.imwrite(img.name, binary_image)

        binary_images.append(binary_image)
        binary_images_path.append(img.name)

    return gr.Image.update(binary_images[0]), gr.Files.update(binary_images_path)

def grayscale(images):
    gray_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(img.name, gray_image)
        gray_images_path.append(img.name)
    return gr.Image.update(cv2.imread(gray_images_path[0], cv2.IMREAD_GRAYSCALE)), gr.Files.update(gray_images_path)

def invert(images):
    inverted_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        inverted_image = cv2.bitwise_not(image)
        cv2.imwrite(img.name, inverted_image)
        inverted_images_path.append(img.name)
    return gr.Image.update(cv2.imread(inverted_images_path[0])), gr.Files.update(inverted_images_path)

def color_remap(images, to_hsv=True):
    converted_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        if to_hsv:
            converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        else:
            converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(img.name, converted_image)
        converted_images_path.append(img.name)
    return gr.Image.update(cv2.imread(converted_images_path[0])), gr.Files.update(converted_images_path)

def blur(images):
    blurred_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
        cv2.imwrite(img.name, blurred_image)
        blurred_images_path.append(img.name)
    return gr.Image.update(cv2.imread(blurred_images_path[0])), gr.Files.update(blurred_images_path)

def descew(images):
    descewed_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        binary_image = cv2.bitwise_not(binary_image)
        coords = np.column_stack(np.where(binary_image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h))

        cv2.imwrite(img.name, rotated)
        descewed_images_path.append(img.name)
    return gr.Image.update(cv2.imread(descewed_images_path[0])), gr.Files.update(descewed_images_path)

def morph(images, inpaint_mask=None):
    morphed_images = []
    morphed_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Opening (オープニング)
        kernel_opening = np.ones((5,5), np.uint8)
        opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel_opening)

        # Closing (クロージング)
        kernel_closing = np.ones((5,5), np.uint8)
        morphed = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_closing)

        # Inpainting (インペイント)
        if inpaint_mask is not None:
            mask = cv2.imread(inpaint_mask[i].name, cv2.IMREAD_GRAYSCALE)
            morphed = cv2.inpaint(morphed, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

        cv2.imwrite(img.name, morphed)
        morphed_images.append(morphed)
        morphed_images_path.append(img.name)

    return gr.Image.update(morphed_images[0]), gr.Files.update(morphed_images_path)

def thin(images):
    thinned_images_path = []
    for i, img in enumerate(images):
        image = cv2.imread(img.name, cv2.IMREAD_GRAYSCALE)
        _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        thinned_image = cv2.ximgproc.thinning(binary_image)
        cv2.imwrite(img.name, thinned_image)
        thinned_images_path.append(img.name)
    return gr.Image.update(cv2.imread(thinned_images_path[0], cv2.IMREAD_GRAYSCALE)), gr.Files.update(thinned_images_path)

def undo_filter():
    global current_image
    current_image = original_image

def undo_add_():
    pass

def undo_remove_():
    pass

def undo_resize():
    pass

def undo_crop():
    pass

def undo_squiz():
    pass

def undo_binarize(original_images):
    original_images_path = []
    for i, img in enumerate(original_images):
        path = f"original_image_{i}.png"
        cv2.imwrite(path, img)
        original_images_path.append(path)
    return gr.Image.update(original_images[0]), gr.Files.update(original_images_path)

def undo_descew():
    pass

def undo_grayscale():
    pass

def undo_invert():
    pass

def undo_blur():
    pass

def undo_color_remap():
    pass

def undo_morph():
    pass

def undo_thin():
    pass



def find_lines(image, thres1=50, thres2=150, thres3=100, line_w_min=50, line_gap_max=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, thres1, thres2, apertureSize=3)
    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi / 180,
        threshold=thres3,
        minLineLength=line_w_min,
        maxLineGap=line_gap_max
        )
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return image

def set_stopwatch():
    start_time = time.time()
    return start_time

def stop_stopwatch(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time: {elapsed_time} sec.")

def time_conversion(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

def detect_circles(image, min_value, max_value):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            x, y, radius = i[0], i[1], i[2]
            image = draw_circle(image, x, y, radius)
            image = draw_gauge_labels(image, x, y, radius, min_value, max_value)
    return image

def avg_circles(circles):
    avg_x, avg_y, avg_radius = 0, 0, 0
    for circle in circles[0, :]:
        avg_x += circle[0]
        avg_y += circle[1]
        avg_radius += circle[2]
    avg_x /= len(circles[0, :])
    avg_y /= len(circles[0, :])
    avg_radius /= len(circles[0, :])
    return avg_x, avg_y, avg_radius

def calibrate_gauge(image, min_value, max_value, min_angle=0, max_angle=180):
    circles = detect_circles(image, min_value, max_value)
    x, y, radius = avg_circles(circles)
    # その他のキャリブレーションパラメータをここで設定
    result = {}
    result['x'] = x
    result['y'] = y
    result['radius'] = radius
    result['min_angle'] = min_angle
    result['max_angle'] = max_angle
    result['min_value'] = min_value
    result['max_value'] = max_value
    return result

def process_needle(image, thres_bin=40, thres_can_from=30, thres_can_end=150, thres_hough=100, min_line_length=10, max_line_gap=250):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(gray_image, thres_bin, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(thresholded_image, thres_can_from, thres_can_end)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=thres_hough, minLineLength=min_line_length, maxLineGap=max_line_gap)
    return lines


def dist_2_pts(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_current_value(image, calibration_data):
    lines = process_needle(image)
    x, y, radius = calibration_data['x'], calibration_data['y'], calibration_data['radius']
    min_angle, max_angle = calibration_data['min_angle'], calibration_data['max_angle']
    min_value, max_value = calibration_data['min_value'], calibration_data['max_value']

    angle = 0
    for line in lines:
        for x1, y1, x2, y2 in line:
            if dist_2_pts(x, y, x1, y1) < radius and dist_2_pts(x, y, x2, y2) < radius:
                angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
                break

    current_value = ((angle - min_angle) / (max_angle - min_angle)) * (max_value - min_value) + min_value
    return current_value

def process_frame(frame, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Processing Frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_circle(image, x, y, radius):
    cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
    cv2.circle(image, (int(x), int(y)), 2, (0, 0, 255), 3)
    return image

def draw_gauge_labels(image, x, y, radius, min_value, max_value):
    # ゲージの目盛りとラベルを描画するコード
    # 例: ゲージの円周上に等間隔でラインと値を描画
    for i in range(0, 11):
        angle = np.pi/2 - i * np.pi/10
        x2 = x + radius * np.cos(angle)
        y2 = y - radius * np.sin(angle)
        cv2.line(image, (int(x), int(y)), (int(x2), int(y2)), (0, 255, 0), 2)
        value = min_value + i * (max_value - min_value) / 10
        cv2.putText(image, str(int(value)), (int(x2), int(y2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    return image

def map_angle_to_value(angle, min_angle, max_angle, min_value, max_value):
    value_range = max_value - min_value
    angle_range = max_angle - min_angle
    value = ((angle - min_angle) * value_range / angle_range) + min_value
    return value

def plot_data(data):
    times, values = zip(*data)
    plt.plot(times, values)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Time vs Value')
    plt.show()

def fit_heating_cooling_curve(data):
    def curve_func(x, a, b, c):
        return a * np.log(b * x) + c

    x_data, y_data = zip(*data)
    params, _ = curve_fit(curve_func, x_data, y_data)
    plt.plot(x_data, y_data, 'b-', label='data')
    plt.plot(x_data, [curve_func(x, *params) for x in x_data], 'r-', label='fit')
    plt.legend()
    plt.show()
    return params

def save_annotated_video(frames, tmpf):
    # height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(tmpf, fourcc, 20.0, (640, 480))

    for frame in frames:
        out.write(frame)
    out.release()

def get_frames(video):
    pass

def bar_plot_fn(display):
    simple = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )
    fake_barley = pd.DataFrame(
        {
            "site": [
                random.choice(
                    [
                        "University Farm",
                        "Waseca",
                        "Morris",
                        "Crookston",
                        "Grand Rapids",
                        "Duluth",
                    ]
                )
                for _ in range(120)
            ],
            "yield": [random.randint(25, 75) for _ in range(120)],
            "variety": [
                random.choice(
                    [
                        "Manchuria",
                        "Wisconsin No. 38",
                        "Glabron",
                        "No. 457",
                        "No. 462",
                        "No. 475",
                    ]
                )
                for _ in range(120)
            ],
            "year": [
                random.choice(
                    [
                        "1931",
                        "1932",
                    ]
                )
                for _ in range(120)
            ],
        }
    )
    if display == "simple":
        return gr.BarPlot.update(
            simple,
            x="a",
            y="b",
            title="Simple Bar Plot with made up data",
            tooltip=["a", "b"],
            y_lim=[20, 100],
        )
    elif display == "stacked":
        return gr.BarPlot.update(
            fake_barley,
            x="variety",
            y="yield",
            color="site",
            title="Barley Yield Data",
            tooltip=["variety", "site"],
        )
    elif display == "grouped":
        return gr.BarPlot.update(
            fake_barley.astype({"year": str}),
            x="year",
            y="yield",
            color="year",
            group="site",
            title="Barley Yield by Year and Site",
            group_title="",
            tooltip=["yield", "site", "year"],
        )
    elif display == "simple-horizontal":
        return gr.BarPlot.update(
            simple,
            x="a",
            y="b",
            x_title="Variable A",
            y_title="Variable B",
            title="Simple Bar Plot with made up data",
            tooltip=["a", "b"],
            vertical=False,
            y_lim=[20, 100],
        )
    elif display == "stacked-horizontal":
        return gr.BarPlot.update(
            fake_barley,
            x="variety",
            y="yield",
            color="site",
            title="Barley Yield Data",
            vertical=False,
            tooltip=["variety", "site"],
        )
    elif display == "grouped-horizontal":
        return gr.BarPlot.update(
            fake_barley.astype({"year": str}),
            x="year",
            y="yield",
            color="year",
            group="site",
            title="Barley Yield by Year and Site",
            group_title="",
            tooltip=["yield", "site", "year"],
            vertical=False,
        )

def main(files, min_value, max_value, min_angle, max_angle):
    images = []
    videos = []
    frames = []
    result = {}
    result_all = []
    start_time = set_stopwatch()

    for file in files:
        if file.name.endswith('.jpg'):
            images.append(cv2.imread(file.name))
        elif file.name.endswith('.mp4'):
            videos.append(cv2.VideoCapture(file.name))
        else:
            raise Exception
    try:
        for i, image in enumerate(images):
            # if resize:
            #     image = cv2.resize(image, (width, height))
            # if crop:
            #     image = image[crop[0]:crop[1], crop[2]:crop[3]]
            # if mask:
            #     image = mask(image, mask)
            # if blur:
            #     image = cv2.GaussianBlur(image, (5, 5), 0)
            # if invert:
            #     image = cv2.bitwise_not(image)

            calibration_data = calibrate_gauge(image, min_value, max_value, min_angle, max_angle)

            current_value = get_current_value(image, calibration_data)

            result[f'image_{i}']['gauge_value'] = current_value

            value = map_angle_to_value(current_value, min_value, max_value)
            result[f'image_{i}']['value'] = value

            process_frame(frame)

        for i, video in enumerate(videos):
            while video.isOpened():
                ret, frame = video.read()
                if not ret:
                    break

                elif ret:
                    frames.append(frame)
                else:
                    break

            start_frame = frames[0]
            for j ,frame in enumerate(frames[start_frame:]):
                # if resize:
                #     image = cv2.resize(image, resize)
                # if crop:
                #     image = image[crop[0]:crop[1], crop[2]:crop[3]]
                # if mask:
                #     image = mask(image, mask)
                # if blur:
                #     image = cv2.GaussianBlur(image, (blur_size, blur_size), 0)
                # if invert:
                #     image = cv2.bitwise_not(image)

                calibration_data = calibrate_gauge(image, min_value, max_value, min_angle, max_angle)
                current_value = get_current_value(image, calibration_data)
                result[f'video_{i}'][f'frame_{j}']['gauge_value'] = current_value

                value = map_angle_to_value(current_value, min_value, max_value)
                result[f'video_{i}'][f'frame_{j}']['value'] = value

                process_frame(frame)

            stop_time = stop_stopwatch(start_time)
            result[f'video_{i}'][f'stop_time'] = stop_time
            result[f'video_{i}'][f'value'] = value

            print(f"Processing completed in {stop_time} seconds.")

    except Exception as e:
        print(e)

    try:
        plot_data(result)
        fit_heating_cooling_curve(result)
        video.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(e)

    zip_path, result_data, data, df = save_dfs(result)
    image_paths = save_images(images)
    video_paths = save_videos(videos, frames)

    return gr.Files.update(zip_path), gr.Image.update(image_paths[0] if image_paths else None), gr.Video.update(video_paths[0] if video_paths else None), gr.TextArea.update(data)


def save_images(images):
    ts, tmpd = Interface.get_tempdir()
    image_paths = []
    for i, image in enumerate(images):
        tmpf = f'{tmpd}/{ts}_{i}.jpg'
        cv2.imwrite(tmpf, image)
        image_paths.append(tmpf)
    return image_paths

def save_videos(videos, frames):
    ts, tmpd = Interface.get_tempdir()
    video_paths = []
    for i, video in enumerate(videos):
        tmpf = f'{tmpd}/{ts}_{i}.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(tmpf, fourcc, 20.0, (640, 480))
        for frame in frames:
            out.write(frame)
        out.release()
        video_paths.append(tmpf)
    return video_paths

def save_dfs(data):
    ts, tmpd = Interface.get_tempdir()
    tmpf = f'{tmpd}/{ts}'
    text_path = f'{tmpf}.txt'
    csv_path = f'{tmpf}.csv'
    json_path = f'{tmpf}.json'
    yaml_path = f'{tmpf}.yaml'
    toml_path = f'{tmpf}.toml'
    xml_path = f'{tmpf}.xml'
    zip_path = f'{tmpf}.zip'

    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False, encoding='utf-8')

    df.to_json(json_path, force_ascii=False)
    # with open(json_path, 'w') as json_file:
    #     json.dump(data, json_file, ensure_ascii=False)

    with open(yaml_path, 'w') as yaml_file:
        yaml.dump(data, yaml_file)

    with open(toml_path, 'w') as toml_file:
        toml_data = {'data': data}
        result_data = toml.dump(toml_data, toml_file)

    Interface.create_zip(zip_path, [toml_path, json_path, csv_path])

    return zip_path, result_data, data, df

def update_preview(files):
    images = []
    videos = []
    for file in files:
        if file.name.endswith('.jpg'):
            images.append(file.name)
        elif file.name.endswith('.mp4'):
            videos.append(file.name)
        else:
            continue

    image_preview = gr.Image.update(images[0]) if images else None
    video_preview = gr.Video.update(videos[0]) if videos else None

    return image_preview, video_preview


def webui():
    version = 'v0.1.0'
    with gr.Blocks(
            css='footer {visibility: hidden}') as app:
        gr.HTML(f"<div style='max-width:100%; max-height:360px; text-align: center; overflow:auto'><h1>Analog Gauge Reader WebUI {version}</h1></div>")
        with gr.Row(variant='panel'):
            upl_btn = gr.UploadButton(file_count="multiple", file_types=['image', 'video'])

            with gr.Row(variant='panel'):
                add_btn = gr.Button('+')
                remove_btn = gr.ClearButton(value='-')
                clr_param_btn = gr.ClearButton(value='×')
                clr_cache_btn = gr.ClearButton(value='C')
                run_btn = gr.Button(value='▶', variant='primary')

        with gr.Tab('Process') as tab1:
            with gr.Row(variant='compact'):
                with gr.Column(variant='panel'):
                    input_images = gr.Image(scale=1)
                    input_videos = gr.Video(scale=1)
                    input_files = gr.Files(visible=False)
                    with gr.Accordion('Parameters', open=False):
                        with gr.Row(variant='panel'):
                            min_value = gr.Number(25, step=1, precision=1, label="Value Min")
                            max_value = gr.Number(55, step=1, precision=1, label="Value Max")
                            min_angle = gr.Number(180, step=1, precision=1, label="angle Min")
                            max_angle = gr.Number(0, step=1, precision=1, label="angle Max")
                            units = gr.Textbox("PSI", label="Unit")

                        filter_functions = {
                            '+': {'apply': add_, 'undo': undo_add_},
                            '-': {'apply': remove_, 'undo': undo_remove_},
                            '☒': {'apply': resize, 'undo': undo_resize},
                            '✂': {'apply': crop, 'undo': undo_crop},
                            '↕️': {'apply': squiz, 'undo': undo_squiz},
                            '◐': {'apply': binarize, 'undo': undo_binarize},
                            '◐': {'apply': grayscale, 'undo': undo_grayscale},
                            '↔': {'apply': invert, 'undo': undo_invert},
                            '⇔': {'apply': color_remap, 'undo': undo_color_remap},
                            '☁️': {'apply': blur, 'undo': undo_blur},
                            '↺': {'apply': descew, 'undo': undo_descew},
                            '⚙': {'apply': morph, 'undo': undo_morph},
                            '✎': {'apply': thin, 'undo': undo_thin},
                        }
                        chks_filter = gr.CheckboxGroup(choices=list(filter_functions.keys()), label="Filter")

                with gr.Column(variant='panel'):
                    output_image = gr.Image()
                    output_video = gr.Video()
                    output_file = gr.Files()
                    output_text = gr.TextArea()
                    output_tree = gr.JSON()

        with gr.Tab('Table'):
            with gr.Row():
                with gr.Column():
                    display = gr.Dropdown(
                        choices=[
                            "simple",
                            "stacked",
                            "grouped",
                            "simple-horizontal",
                            "stacked-horizontal",
                            "grouped-horizontal",
                        ],
                        value="simple",
                        label="Type of Bar Plot",
                    )
                    output_bar = gr.BarPlot()
                    display.change(bar_plot_fn, inputs=display, outputs=output_bar)

                with gr.Column():
                    display2 = gr.Dropdown(
                        choices=[
                            "simple",
                            "stacked",
                            "grouped",
                            "simple-horizontal",
                            "stacked-horizontal",
                            "grouped-horizontal",
                        ],
                        value="simple",
                        label="Type of Bar Plot",
                    )
                    output_bar2 = gr.BarPlot()
                    display2.change(bar_plot_fn, inputs=display2, outputs=output_bar2)
            output_table = gr.Dataframe(max_rows=10, max_cols=10, interactive=True)

        with gr.Tab('Gallery'):
            output_mask = gr.Gallery()

        with gr.Tab('Preferences'):
            with gr.Row(variant='compact'):
                with gr.Column(variant='panel', scale=1):
                    export_btn = gr.Button('Export settings')
                    # btn_login = gr.LoginButton()
                    # btn_logout = gr.LogoutButton()
                with gr.Column(variant='panel', scale=4):
                    tmpd = gr.Textbox(f'', label="temp_dir")
                    ts = gr.Textbox(f'', label="ts")
                    tmpf = gr.Textbox(f'', label="temp_file")
                    csv_path = gr.Textbox(f'.csv', label="csv_path")
                    json_path = gr.Textbox(f'.json', label="json_path")
                    text_path = gr.Textbox(f'.txt', label="text_path")
                    zip_path = gr.Textbox(f'.zip', label="zip_path")

        with gr.Tab('Help'):
            with gr.Row(variant='compact'):
                with gr.Column(variant='panel', scale=1):
                    gr.Text('test')

        inputs = [input_files, min_value, max_value, min_angle, max_angle]

        outputs = [output_file, output_image, output_video, output_text]

        with tab1:
            examples = [
                [['images/demo.jpg'], -25, 55, 180, 0],
                [['videos/demo.mp4'], -25, 55, 180, 0],
                [['images/demo.jpg', 'videos/demo.mp4'], -25, 55, 180, 0]
                ]

            examples = gr.Examples(examples,
             [input_files, min_value, max_value, min_angle, max_angle],
             [input_files, input_images, input_videos, min_value, max_value]
             )

        input_files.change(update_preview, input_files, [input_images, input_videos])

        upl_btn.upload(Interface.upload_file, upl_btn, [input_files, input_images, input_videos])

        # chks_filter.select(lambda evt: apply_filter(evt, filter_functions), input_images, input_images)
        run_btn.click(main, inputs, outputs)

        app.load()

    app.launch(
        # inline=True,
        inbrowser=False,
        # share=True,
        # debug=True,
        # max_threads=40,
        # auth=('test','pass'),
        # auth_message=auth_message,
        # prevent_thread_lock=False,
        show_error=True,
        server_name=None,
        # server_port=None,
        # show_tips=False,
        # height=,
        # width=,
        # encrypt=,
        # favicon_path="assets/favicon.ico",
        ssl_keyfile=None,
        ssl_certfile=None,
        ssl_keyfile_password=None,
        ssl_verify=True,
        quiet=False,
        # show_api=False,
        # file_directories=False,
        # allowed_paths=False,
        # blocked_paths=False,
        # root_path=False,
        # app_kwargs=False,
        )


if __name__ == '__main__':
    webui()