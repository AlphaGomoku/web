from alphagomoku import create_app

app = create_app()
app.run(host='0.0.0.0', threaded=True, processes=1, use_reloader=False)