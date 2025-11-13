"""
提示词模板模块
用于生成不同主题的文章提示词
"""

def generate_prompt(keyword: str, description: str, word_count: int = 200) -> str:
    """
    生成文章提示词

    Args:
        keyword: 主题关键词
        description: 主题描述
        word_count: 目标字数

    Returns:
        完整的提示词
    """
    prompt = f"""Write an English essay about "{keyword}" for CET-6 (College English Test Band 6), approximately {word_count} words.

Topic: {keyword}
Description: {description}

IMPORTANT REQUIREMENTS:
1. Format:
   - First line: A clear, engaging title (do NOT write "Title:" before it)
   - Then a blank line
   - Then 2-4 paragraphs of content
   - Separate each paragraph with a blank line

2. Content Structure (flexible, 2-4 paragraphs total):
   - Begin with introduction of the topic and main idea
   - Develop your arguments with examples and analysis (can be 1-2 paragraphs)
   - End with conclusion or insights
   - The exact number of paragraphs depends on your content organization

3. Language Requirements:
   - Use CET-6 level vocabulary (college-level academic English)
   - Include varied sentence structures (simple, compound, complex sentences)
   - Use transitional words: however, moreover, furthermore, in addition, for instance, etc.
   - Provide specific examples to support your points

4. What NOT to do:
   - Do NOT write labels like "Title:", "Introduction:", "Body:", "Conclusion:"
   - Do NOT use Chinese characters
   - Do NOT write meta-commentary about the essay

Example format (you can use 2, 3, or 4 paragraphs as needed):

The Impact of Technology on Education

Technology has revolutionized the way we learn and teach. [Continue with introduction...]

Furthermore, digital tools have enabled personalized learning experiences. [Develop your argument...]

In conclusion, while technology presents challenges, its benefits are undeniable. [Conclude your essay...]

Now write your essay:"""

    return prompt


def generate_subtopic_prompt(main_keyword: str, sub_keyword: str, word_count: int = 200) -> str:
    """
    生成子主题文章提示词

    Args:
        main_keyword: 主主题关键词
        sub_keyword: 子主题关键词
        word_count: 目标字数

    Returns:
        完整的提示词
    """
    prompt = f"""Write an English essay about "{sub_keyword}" (related to "{main_keyword}") for CET-6 (College English Test Band 6), approximately {word_count} words.

Main Topic: {main_keyword}
Subtopic: {sub_keyword}

IMPORTANT REQUIREMENTS:
1. Format:
   - First line: A clear, engaging title (do NOT write "Title:" before it)
   - Then a blank line
   - Then 2-4 paragraphs of content
   - Separate each paragraph with a blank line

2. Content Structure (flexible, 2-4 paragraphs total):
   - Begin with introduction of the subtopic and main idea
   - Develop your arguments with examples and analysis (can be 1-2 paragraphs)
   - End with conclusion or insights
   - The exact number of paragraphs depends on your content organization

3. Language Requirements:
   - Use CET-6 level vocabulary (college-level academic English)
   - Include varied sentence structures (simple, compound, complex sentences)
   - Use transitional words: however, moreover, furthermore, in addition, for instance, etc.
   - Provide specific examples to support your points

4. What NOT to do:
   - Do NOT write labels like "Title:", "Introduction:", "Body:", "Conclusion:"
   - Do NOT use Chinese characters
   - Do NOT write meta-commentary about the essay

Example format (you can use 2, 3, or 4 paragraphs as needed):

The Impact of Technology on Education

Technology has revolutionized the way we learn and teach. [Continue with introduction...]

Furthermore, digital tools have enabled personalized learning experiences. [Develop your argument...]

In conclusion, while technology presents challenges, its benefits are undeniable. [Conclude your essay...]

Now write your essay:"""

    return prompt

