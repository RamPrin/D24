import requests
import json
import re
import os
import time

def write_this_down(system: str):
    text = json.loads(open(f"data/{system}/response.json").read())["response"]
    with open(f"data/{system}/response.md", 'w') as f:
        f.write(text)
    model : list[re.Match[str]] = re.findall(r"# Model:\n```python([\S\s]*?)\n```", text)
    if len(model) != 0:
        with open(f"data/{system}/model.py", "w") as f:
            f.write(model[0])
    else:
        raise Exception("Failed to get model code :(")

def get_description(system: str):
    data = open(f"data/{system}/description.md").read()
    response = requests.post(
        "http://ec2-13-53-134-5.eu-north-1.compute.amazonaws.com:8000/one_agent",
        json={
            "description": data
        }
    )
    try:    
        with open(f"data/{system}/response.json", "w") as f:
            f.write(json.dumps(response.json()))
        write_this_down(system)
    except Exception as e:
        print(e)

def modelize_analyze(system: str):
    data = open(f"data/{system}/description.md").read()
    response = requests.post(
        "http://ec2-13-53-134-5.eu-north-1.compute.amazonaws.com:8000/modelize",
        json={
            "description": data
        }
    ).json()
    print(response)
    text = response["model"]
    model: list[re.Match[str]] = re.findall(r"# Model:\n```python([\S\s]*?)\n```", text)
    if len(model) != 0:
        with open(f"data/{system}/model_2.py", "w") as f:
            f.write(model[0])
        response = requests.post(
            "http://ec2-13-53-134-5.eu-north-1.compute.amazonaws.com:8000/analyze",
            json={
                "model": model[0]
            }).json()
        with open(f"data/{system}/response_2.md", "w") as f:
            f.write(response["threats"])
    else:
        raise Exception("Failed to get model code :(")

if __name__ == "__main__":
    # for (_, fold, file) in os.walk("data/"):
    #     for system in fold:
    #         if os.path.exists(f"data/{system}/description.md"):
    #             modelize_analyze(system)
    #             time.sleep(2)
    #     break
    # modelize_analyze("s3")
    data = open("./data/s3/description.md").read()
    print(json.dumps({"description": data, "model": "gpt-4o"}))

    # response = get_description("oauth2.0")
    # write_this_down("oauth2.0")