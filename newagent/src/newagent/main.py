#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from newagent.crews.poem_crew.poem_crew import PoemCrew
from newagent.crews.blog_crew.blog_crew import BlogCrew


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class BlogState(BaseModel):
    topic: str = ""
    word_count: int = 800
    blog_post: str = ""


class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"sentence_count": self.state.sentence_count})
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)


class BlogFlow(Flow[BlogState]):
    
    @start()
    def set_blog_parameters(self):
        print("Setting blog parameters")
        self.state.topic = "The Future of Artificial Intelligence"
        self.state.word_count = 800

    @listen(set_blog_parameters)
    def generate_blog(self):
        print("Generating blog post")
        result = (
            BlogCrew()
            .crew()
            .kickoff(inputs={
                "topic": self.state.topic,
                "word_count": self.state.word_count
            })
        )
        
        print("Blog post generated")
        self.state.blog_post = result.raw

    @listen(generate_blog)
    def save_blog(self):
        print("Saving blog post")
        with open("blog_post.md", "w") as f:
            f.write(self.state.blog_post)


def kickoff():
    # You can choose which flow to run
    blog_flow = BlogFlow()
    blog_flow.kickoff()


def plot():
    blog_flow = BlogFlow()
    blog_flow.plot()


if __name__ == "__main__":
    kickoff()
