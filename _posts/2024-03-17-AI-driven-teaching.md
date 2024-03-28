---
title: AI-Driven Teaching and Learning Experience
layout: post
---

![ai-teacher](https://i0.wp.com/calmatters.org/wp-content/uploads/2022/06/060623-Professor-AI-Midjourney-CM-01.jpg?w=2000&ssl=1)

*The image was take from [calmatters.org](https://calmatters.org/){:target="_blank"}*

This is the third year that I am giving the ININ tutorial. With the advances in AI, I am always looking for ways to improve the teaching experience. Last year, I have used the GitHub Copilot to show students how programming can be made easier with AI. This year, I am going to make the course more interactive by constructing a website that students can use to follow the course material, follow the links to interact with ChatGPT and run the code in a Jupyter notebook environment.

This kind of setup has been my dream for a long time because it allows me to focus on the content of the course and not on the technical details of setting up the lab environment. At the same time, it allows the students to access the course material from anywhere and at any time in a way that is interactive and engaging.



When you are giving a course that will use programming, you basically want to:

1. Have a website where you can post the course material.
2. Have a repository where you can store the code and exercises.
3. configure lab environments for the students to run jupyter notebooks.
4. students could start the lab environment with a single click (probably the most important feature).

How can you do that in the simplest way possible? Here is a suggestion:

1. Create a GitHub repository for the course.
2. Create a GitHub Pages website for the course with _jekyll minima_ theme.
3. Create a _Dockerfile_ that installs the necessary packages for the lab environment.
4. Setup the github respository as a template repository.

You can visit [this repository](https://github.com/oceanumeric/ININ-tutorial){:target="_blank"} to see an example of how to do this.


For the theme of the course website, I have chosen the _jekyll minima_ theme. It is a simple and clean theme that is easy to customize. We say the simplest way is the best way. With this theme and default settings from Github, you do not need any CICD pipeline to build the website. You can just push the changes to the repository and the website will be updated automatically.

As it shows in the rest of this page, you can show code snippets in different languages, write math equations, and even include images. This is a great way to make the course material more interactive and engaging.


You can write `python` code:

```python
def hello():
    print("Hello, World!")
```

You can write `bash` code:

```bash
echo "Hello, World!"
```

You can write `sql` code:

```sql
SELECT * FROM table
WHERE column = 'value';
```

Let's try some math:

$$
\begin{align*}
\frac{1}{2} + \frac{1}{3} &= \frac{5}{6} \\
\end{align*}
$$

You can even do math inline: $1 + 1 = 2$ or matrix multiplication:

$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
=
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}
$$


## Using ChatGPT in the Course

From time to time, I will share links like this one:

- [ChatGPT Reading Mater](https://chat.openai.com/share/6cb183e1-68de-41a3-837a-50a4d2482bc9)

You can click on the link and interact with ChatGPT. It is a great way to learn new things and get help with the course material.
