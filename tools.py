from dotenv import load_dotenv
load_dotenv()

from crewai_tools import YoutubeChannelSearchTool

yt_tool = YoutubeChannelSearchTool(
    youtube_channel_url="https://www.youtube.com/@3blue1brown"
)
