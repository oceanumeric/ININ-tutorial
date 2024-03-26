---
title: AI-driven teaching with Copilot, ChatGPT and GitHub
layout: post
---


This is the third year that I am giving the ININ tutorial. With the advances in AI, I am always looking for ways to improve the teaching experience. Last year, I have used the GitHub Copilot to show students how programming can be made easier with AI. This year, I am going to make the course more interactive by constructing a website that students can use to follow the course material, follow the links to interact with ChatGPT and run the code in a Jupyter notebook environment.



When you are giving a course that will use programming, you basically want to:

1. Have a website where you can post the course material.
2. Have a repository where you can store the code and exercises.
3. configure lab environments for the students to run jupyter notebooks.

How can you do that in the simplest way possible? Here is a suggestion:

1. Create a GitHub repository for the course.
2. Create a GitHub Pages website for the course with _jekyll minima_ theme.
3. Create a _Dockerfile_ that installs the necessary packages for the lab environment.
4. Setup the github respository as a template repository.

You can visit [this repository](https://github.com/oceanumeric/ININ-tutorial) to see an example of how to do this.




This is an example post.

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