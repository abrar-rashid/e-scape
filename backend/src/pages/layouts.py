from src.pages.pageTypes import PageType


front_with_story_layouts = [
    {
        "elements": [
            {
                "name": "paper_box",
                "type": "B",
                "x1": 210.0,
                "y1": 82.53919239904988,
                "x2": 420.0,
                "y2": 165.07838479809976,
                "rotate": -180,
                "priority": 1,
                "size": 1.5
            },
            {
                "name": "paper",
                "type": "I",
                "x1": 210.0,
                "y1": 82.53919239904988,
                "x2": 420.0,
                "y2": 82.53919239904988,
                "rotate": -180,
                "priority": 1,
                "keep_aspect_ratio": True
            },
            {
                "name": "header",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 12.34560570071259,
                "x2": 146.11764705882354,
                "y2": 31.39311163895487,
                "rotate": 0,
                "multiline": False,
                "size": 30,
                "priority": 2
            },
            {
                "name": "intro",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 34.56769596199525,
                "x2": 146.11764705882354,
                "y2": 38.56769596199525,
                "rotate": 0,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "reqs",
                "type": "T",
                "x1": 152.11764705882354,
                "y1": 12.34560570071259,
                "x2": 201.88235294117646,
                "y2": 18.34560570071259,
                "rotate": 0,
                "multiline": True,
                "size": 18,
                "priority": 2
            },
            {
                "name": "title",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 85.71377672209026,
                "x2": 146.11764705882354,
                "y2": 99.47030878859857,
                "rotate": 0,
                "multiline": False,
                "size": 20,
                "priority": 2
            },
            {
                "name": "story",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 102.64489311163896,
                "x2": 201.88235294117646,
                "y2": 106.64489311163896,
                "rotate": 0,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_1_text",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 139.68171021377674,
                "x2": 67.05882352941177,
                "y2": 143.68171021377674,
                "rotate": 0,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_1_image",
                "type": "I",
                "x1": 12.352941176470589,
                "y1": 139.68171021377674,
                "x2": 67.05882352941177,
                "y2": 185.53681710213777,
                "rotate": 0,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "hint_2_text",
                "type": "T",
                "x1": 66.70588235294117,
                "y1": 215.5190023752969,
                "x2": 134.8235294117647,
                "y2": 219.5190023752969,
                "rotate": -90,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_2_image",
                "type": "I",
                "x1": 66.70588235294117,
                "y1": 215.5190023752969,
                "x2": 134.8235294117647,
                "y2": 270.19239904988126,
                "rotate": -90,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "puzzle_text",
                "type": "T",
                "x1": 71.64705882352942,
                "y1": 139.68171021377674,
                "x2": 201.8823529411765,
                "y2": 147.68171021377674,
                "rotate": 0,
                "multiline": True,
                "size": 25,
                "priority": 2
            },
            {
                "name": "puzzle_image",
                "type": "I",
                "x1": 71.64705882352942,
                "y1": 139.68171021377674,
                "x2": 201.8823529411765,
                "y2": 269.83966745843236,
                "rotate": 0,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "page_no",
                "type": "T",
                "x1": 193.05882352941177,
                "y1": 279.0106888361045,
                "x2": 201.88235294117646,
                "y2": 287.8289786223278,
                "rotate": 0,
                "multiline": False,
                "size": 8,
                "priority": 2
            }
        ],
        "graphic_count": 0,
        "has_paper": True
    }]

front_no_story_layouts = [
    {
        "elements": [
            {
                "name": "header",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 12.34560570071259,
                "x2": 146.11764705882354,
                "y2": 31.39311163895487,
                "rotate": 0,
                "multiline": False,
                "size": 30,
                "priority": 2
            },
            {
                "name": "title",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 39.50593824228029,
                "x2": 146.11764705882354,
                "y2": 53.2624703087886,
                "rotate": 0,
                "multiline": False,
                "size": 20,
                "priority": 2
            },
            {
                "name": "reqs",
                "type": "T",
                "x1": 152.11764705882354,
                "y1": 12.34560570071259,
                "x2": 201.88235294117646,
                "y2": 18.34560570071259,
                "rotate": 0,
                "multiline": True,
                "size": 18,
                "priority": 2
            },
            {
                "name": "hint_1_text",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 159.08194774346794,
                "x2": 102.70588235294119,
                "y2": 163.08194774346794,
                "rotate": 85,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_1_image",
                "type": "I",
                "x1": 12.352941176470589,
                "y1": 159.08194774346794,
                "x2": 102.70588235294119,
                "y2": 194.35510688836104,
                "rotate": 85,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "hint_2_text",
                "type": "T",
                "x1": 20.11764705882353,
                "y1": 214.81353919239905,
                "x2": 110.47058823529412,
                "y2": 218.81353919239905,
                "rotate": -24,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_2_image",
                "type": "I",
                "x1": 20.11764705882353,
                "y1": 214.81353919239905,
                "x2": 110.47058823529412,
                "y2": 250.08669833729215,
                "rotate": -24,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "puzzle_text",
                "type": "T",
                "x1": 62.82352941176471,
                "y1": 84.65558194774347,
                "x2": 193.05882352941177,
                "y2": 92.65558194774347,
                "rotate": 0,
                "multiline": True,
                "size": 25,
                "priority": 2
            },
            {
                "name": "puzzle_image",
                "type": "I",
                "x1": 62.82352941176471,
                "y1": 84.65558194774347,
                "x2": 193.05882352941177,
                "y2": 214.81353919239905,
                "rotate": 0,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "graphic_0",
                "type": "I",
                "x1": 114.3529411764706,
                "y1": 235.624703087886,
                "x2": 189.88235294117646,
                "y2": 297.0,
                "rotate": 0,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "page_no",
                "type": "T",
                "x1": 193.05882352941177,
                "y1": 279.0106888361045,
                "x2": 201.88235294117646,
                "y2": 287.8289786223278,
                "rotate": 0,
                "multiline": False,
                "size": 8,
                "priority": 2
            }
        ],
        "graphic_count": 1,
        "has_paper": False
    }]

puzzle_with_story_layouts = [
    {
        "elements": [
            {
                "name": "title",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 12.34560570071259,
                "x2": 146.11764705882354,
                "y2": 26.102137767220903,
                "rotate": 0,
                "multiline": False,
                "size": 20,
                "priority": 1
            },
            {
                "name": "story",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 29.629453681710213,
                "x2": 201.88235294117646,
                "y2": 33.62945368171022,
                "rotate": 0,
                "multiline": True,
                "size": 15,
                "priority": 1
            },
            {
                "name": "hint_1_text",
                "type": "T",
                "x1": 47.64705882352941,
                "y1": 123.10332541567696,
                "x2": 137.64705882352942,
                "y2": 127.10332541567696,
                "rotate": -90,
                "multiline": True,
                "size": 15,
                "priority": 1
            },
            {
                "name": "hint_1_image",
                "type": "I",
                "x1": 47.64705882352941,
                "y1": 123.10332541567696,
                "x2": 137.64705882352942,
                "y2": 158.37648456057008,
                "rotate": -90,
                "priority": 1,
                "keep_aspect_ratio": True
            },
            {
                "name": "hint_2_text",
                "type": "T",
                "x1": 110.47058823529413,
                "y1": 262.7850356294537,
                "x2": 200.82352941176472,
                "y2": 266.7850356294537,
                "rotate": 30,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_2_image",
                "type": "I",
                "x1": 110.47058823529413,
                "y1": 262.7850356294537,
                "x2": 200.82352941176472,
                "y2": 298.0581947743468,
                "rotate": 30,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "paper_box",
                "type": "B",
                "x1": 22.941176470588236,
                "y1": 297.0,
                "x2": 232.94117647058823,
                "y2": 594.0,
                "rotate": 30,
                "priority": 1,
                "size": 1.5
            },
            {
                "name": "paper",
                "type": "I",
                "x1": 22.941176470588236,
                "y1": 297.0,
                "x2": 232.94117647058823,
                "y2": 297.0,
                "rotate": 30,
                "priority": 1,
                "keep_aspect_ratio": True
            },
            {
                "name": "graphic_0",
                "type": "I",
                "x1": 6.705882352941177,
                "y1": 231.3919239904988,
                "x2": 74.47058823529412,
                "y2": 296.29453681710214,
                "rotate": -17,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "puzzle_text",
                "type": "T",
                "x1": 60.00000000000001,
                "y1": 70.54631828978623,
                "x2": 190.23529411764707,
                "y2": 78.54631828978623,
                "rotate": 0,
                "multiline": True,
                "size": 25,
                "priority": 1
            },
            {
                "name": "puzzle_image",
                "type": "I",
                "x1": 60.00000000000001,
                "y1": 70.54631828978623,
                "x2": 190.23529411764707,
                "y2": 200.70427553444182,
                "rotate": 0,
                "priority": 1,
                "keep_aspect_ratio": True
            },
            {
                "name": "page_no",
                "type": "T",
                "x1": 193.05882352941177,
                "y1": 279.0106888361045,
                "x2": 201.88235294117646,
                "y2": 287.8289786223278,
                "rotate": 0,
                "multiline": False,
                "size": 8,
                "priority": 2
            }
        ],
        "graphic_count": 1,
        "has_paper": True
    }]

puzzle_no_story_layouts = [
    {
        "elements": [
            {
                "name": "title",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 12.34560570071259,
                "x2": 146.11764705882354,
                "y2": 26.102137767220903,
                "rotate": 0,
                "multiline": False,
                "size": 20,
                "priority": 2
            },
            {
                "name": "graphic_0",
                "type": "I",
                "x1": 160.94117647058823,
                "y1": 0.0,
                "x2": 210.35294117647058,
                "y2": 52.204275534441805,
                "rotate": 5,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "puzzle_text",
                "type": "T",
                "x1": 12.352941176470589,
                "y1": 43.73871733966746,
                "x2": 142.58823529411765,
                "y2": 51.73871733966746,
                "rotate": 0,
                "multiline": True,
                "size": 25,
                "priority": 2
            },
            {
                "name": "puzzle_image",
                "type": "I",
                "x1": 12.352941176470589,
                "y1": 43.73871733966746,
                "x2": 142.58823529411765,
                "y2": 173.89667458432305,
                "rotate": 0,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "hint_1_text",
                "type": "T",
                "x1": 198.3529411764706,
                "y1": 124.16152019002375,
                "x2": 288.3529411764706,
                "y2": 128.16152019002374,
                "rotate": -90,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_1_image",
                "type": "I",
                "x1": 198.3529411764706,
                "y1": 124.16152019002375,
                "x2": 288.3529411764706,
                "y2": 159.43467933491686,
                "rotate": -90,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "graphic_1",
                "type": "I",
                "x1": -28.23529411764706,
                "y1": 211.28622327790976,
                "x2": 37.05882352941177,
                "y2": 276.54156769596204,
                "rotate": 25,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "paper_box",
                "type": "B",
                "x1": -9.882352941176471,
                "y1": 198.58788598574822,
                "x2": 200.11764705882354,
                "y2": 495.58788598574824,
                "rotate": -15,
                "priority": 1,
                "size": 1.5
            },
            {
                "name": "paper",
                "type": "I",
                "x1": -9.882352941176471,
                "y1": 198.58788598574822,
                "x2": 200.11764705882354,
                "y2": 198.58788598574822,
                "rotate": -15,
                "priority": 1,
                "keep_aspect_ratio": True
            },
            {
                "name": "hint_2_text",
                "type": "T",
                "x1": 83.64705882352942,
                "y1": 234.21377672209027,
                "x2": 174.0,
                "y2": 238.21377672209027,
                "rotate": -15,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "hint_2_image",
                "type": "I",
                "x1": 83.64705882352942,
                "y1": 234.21377672209027,
                "x2": 174.0,
                "y2": 269.4869358669834,
                "rotate": -15,
                "priority": 2,
                "keep_aspect_ratio": True
            },
            {
                "name": "page_no",
                "type": "T",
                "x1": 193.05882352941177,
                "y1": 279.0106888361045,
                "x2": 201.88235294117646,
                "y2": 287.8289786223278,
                "rotate": 0,
                "multiline": False,
                "size": 8,
                "priority": 2
            }
        ],
        "graphic_count": 2,
        "has_paper": True
    }
]

conclusions = [
    {
        "elements": [
            {
                "name": "title",
                "type": "T",
                "x1": 10.23529411764706,
                "y1": 37.03681710213777,
                "x2": 171.5294117647059,
                "y2": 53.61520190023753,
                "rotate": 0,
                "multiline": False,
                "size": 20,
                "priority": 2
            },
            {
                "name": "story",
                "type": "T",
                "x1": 10.23529411764706,
                "y1": 68.42992874109264,
                "x2": 199.76470588235296,
                "y2": 72.42992874109264,
                "rotate": 0,
                "multiline": True,
                "size": 15,
                "priority": 2
            },
            {
                "name": "graphic_0",
                "type": "I",
                "x1": 4.9411764705882355,
                "y1": 184.478622327791,
                "x2": 110.11764705882354,
                "y2": 293.11995249406175,
                "rotate": 3,
                "priority": 1,
                "keep_aspect_ratio": True
            },
            {
                "name": "page_no",
                "type": "T",
                "x1": 193.05882352941177,
                "y1": 279.0106888361045,
                "x2": 201.88235294117646,
                "y2": 287.8289786223278,
                "rotate": 0,
                "multiline": False,
                "size": 8,
                "priority": 2
            }
        ],
        "graphic_count": 1,
        "has_paper": False
    },
]


layout_map = {
    PageType.FRONT_NO_STORY: front_no_story_layouts,
    PageType.FRONT_WITH_STORY: front_with_story_layouts,
    PageType.PUZZLE_NO_STORY: puzzle_no_story_layouts,
    PageType.PUZZLE_WITH_STORY: puzzle_with_story_layouts,
    PageType.CONCLUSION: conclusions,
}
