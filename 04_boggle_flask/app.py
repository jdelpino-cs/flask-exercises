from flask import Flask, request, render_template, session, redirect, jsonify
from boggle import Boggle

boggle_game = Boggle()
