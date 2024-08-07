""" Example handler file. """

from transformers import pipeline
import runpod

pipe = pipeline("text2text-generation", model="google/flan-t5-large")


def handler(job):
    job_input = job['input']
    message = job_input.get('message', 'Hi!')
    return pipe(message)


runpod.serverless.start({"handler": handler})