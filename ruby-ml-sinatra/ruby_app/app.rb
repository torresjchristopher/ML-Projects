require 'sinatra'
require 'json'
require 'httparty'

set :bind, '0.0.0.0'
set :port, 4567

posts = []

get '/' do
  erb :index, locals: { posts: posts }
end

post '/submit' do
  content = params[:content]
  
  response = HTTParty.post("http://localhost:8000/sentiment", 
    body: { text: content }.to_json,
    headers: { 'Content-Type' => 'application/json' })

  sentiment = JSON.parse(response.body)["sentiment"]

  posts << { content: content, sentiment: sentiment }
  redirect '/'
end
