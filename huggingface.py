import bmf

graph = bmf.graph()

video = graph.decode({
     "input_path": "/Users/bytedance/BMF-projects/huggingface-demo/new_test.mp4"
})

bmf.encode(
     video['video'],
     video['audio'],
     {
         "output_path": "/Users/bytedance/BMF-projects/huggingface-demo",
         "video_params": {
             "codec": "h264",
             "width": 320,
             "height": 240,
             "crf": 23,
             "preset": "veryfast"
         },
         "audio_params": {
             "codec": "aac",
             "bit_rate": 128000,
             "sample_rate": 44100,
             "channels": 2
         }
     }
).run()