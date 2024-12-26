import os
import pygame
import time
import random

def play_audio_files(directory, delay=1):
    """
    指定したディレクトリ内の音声ファイルをランダムな順序で再生する。

    Args:
        directory (str): 音声ファイルが保存されているディレクトリ。
        delay (float): 各ファイルの再生間隔（秒単位）。
    """
    # pygame初期化
    pygame.mixer.init()
    
    # ディレクトリ内の音声ファイルをリストアップ（.mp3 または .wav のみ）
    files = sorted([f for f in os.listdir(directory) if f.endswith(('.mp3', '.wav'))])
    
    # 再生順序をランダムにシャッフル
    random.shuffle(files)
    print(f"ランダムな再生順序: {files}")

    # ファイルごとに再生
    for file in files:
        file_path = os.path.join(directory, file)
        print(f"再生中: {file_path}")
        
        # 音声ファイルをロードして再生
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # 再生が終了するまで待機
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        # 再生間隔を適用
        print(f"次の音声まで{delay}秒間待機します...")
        time.sleep(delay)

    print("全ての音声ファイルを再生しました。")
    pygame.mixer.quit()

# 使用例
directory = "audio_files"  # 音声ファイルが保存されているディレクトリ
delay_between_files = 1.0  # 各ファイルの再生間隔（秒）

play_audio_files(directory, delay_between_files)
