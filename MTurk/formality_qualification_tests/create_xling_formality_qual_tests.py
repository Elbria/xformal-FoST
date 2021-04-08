#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: eleftheria
"""

import argparse
import boto3


def main():

   """
   Code for creating a qualification type at Amazon Mechanical Turk
   Important Note: Do not hard code the key and secret_key arguments
   """

   parser = argparse.ArgumentParser(description='Amazon Mechanical turk qualification test creation through boto3 api')
   parser.add_argument('--questions', help='qualification questions (xml file)')
   parser.add_argument('--answers', help='answers to qualification questions (xml file)')
   args = parser.parse_args()

   mturk = boto3.client('mturk',
                         region_name='us-east-1',
                         endpoint_url='https://mturk-requester.us-east-1.amazonaws.com')


   questions = open(args.questions, mode='r').read()
   answers = open(args.answers, mode='r').read()


   qual_response = mturk.create_qualification_type(
                           Name='French formality qualification test',
                           Keywords='test, qualification, french, formality, formal, informal, style',
                           Description='This is a qualification test for the French Formality task',
                           QualificationTypeStatus='Active',
                           Test=questions,
                           AnswerKey=answers,
                           TestDurationInSeconds=600)

   print(qual_response['QualificationType']['QualificationTypeId'])


if __name__ == '__main__':
    main ()