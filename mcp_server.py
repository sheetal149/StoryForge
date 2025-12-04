from mcp.server.fastmcp import FastMCP
from core_functions import get_realtime_info,generate_video_transcription


mcp = FastMCP("This is for Video Script Generator")

@mcp.tool()
async def get_latest_info_mcp(query: str) -> str:
    return get_realtime_info(query)

@mcp.tool()
async def generate_video_script_mcp(query: str) -> str:
    real_info = get_realtime_info(query)
    return generate_video_transcription(real_info)

if __name__ == "__main__":
    mcp.run(transport="stdio")



#     **(Scene: Opens with a montage of fast-paced fashion show clips, magazine covers, and protest signs with slogans about ethical fashion.)**

# **(Upbeat, trendy music playing in the background)**

# **Voiceover:** Hey fashion lovers! Ever wonder what's REALLY trending? It's not just about the clothes anymore! 🤯

# **(Scene changes to a close-up of a person looking thoughtful.)**

# **Voiceover:** We're talking ethics, sustainability, and *real* representation! Fashion is evolving, pushed by movements like Fashion Revolution that demand transparency.

# **(Scene shows quick shots of diverse models, sustainable clothing labels, and recycled materials.)**

# **Voiceover:** So, before you click "add to cart," ask yourself: Where did this come from? And what's it made of?

# **(Scene focuses on the speaker, smiling.)**

# **Voiceover:** Want to be a conscious consumer? Follow us for more tips on building a stylish AND sustainable wardrobe! #EthicalFashion #SustainableStyle #FashionRevolution
