import gradio as gr
import requests

def get_twitter_user_info(username):
    # Check if the input is a URL, if so, extract the username
    if "twitter.com/" in username:
        username = username.split("/")[-1]

    # Fetch user data from Twitter API
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {
        "Authorization": "Bearer YOUR_TWITTER_API_KEY"  # Replace with your Twitter API key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get("data")
        return {
            "Icon thumbnail": data.get("profile_image_url"),
            "STATUS": "Success",
            "TWITTER ID": data.get("id"),
            "TWITTER USERNAME": data.get("username"),
            "TWITTER DESCRIPTION": data.get("description"),
            "FOLLOWER COUNT": data.get("public_metrics", {}).get("followers_count"),
            "DATE CREATE": data.get("created_at")
        }
    else:
        return {
            "Icon thumbnail": "",
            "STATUS": "Failed",
            "TWITTER ID": "",
            "TWITTER USERNAME": "",
            "TWITTER DESCRIPTION": "",
            "FOLLOWER COUNT": "",
            "DATE CREATE": ""
        }

iface = gr.Interface(get_twitter_user_info, 
                      gr.Textbox(label="Twitter username or profile URL"), 
                      [gr.Image(label="Icon thumbnail"),
                       gr.Textbox(label="STATUS"),
                       gr.Textbox(label="TWITTER ID"),
                       gr.Textbox(label="TWITTER USERNAME"),
                       gr.Textbox(label="TWITTER DESCRIPTION"),
                       gr.Textbox(label="FOLLOWER COUNT"),
                       gr.Textbox(label="DATE CREATE")],
                      title="Twitter User Info Finder",
                      description="Enter a Twitter username or profile URL to get user information.",
                      examples=['elonmusk'])

iface.launch()
