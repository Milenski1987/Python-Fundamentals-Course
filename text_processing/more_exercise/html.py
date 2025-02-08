

article_title = input()
article_content = input()
article_comments = []

while True:
    comment = input()

    if comment == "end of comments":
        break

    article_comments.append(comment)

print(f"<h1>\n    {article_title}\n</h1>")
print(f"<article>\n    {article_content}\n</article>")
for current_comment in article_comments:
    print(f"<div>\n    {current_comment}\n</div>")