# Holiday Photo App – Ballylinny Version (Production Ready)

## How to Run Locally

1. Make sure Python is installed.
2. Install Flask and Gunicorn:
   ```
   pip install flask gunicorn
   ```

3. Run the app (for testing only):
   ```
   python app.py
   ```

## How to Host on Render

1. Upload this folder to a GitHub repository.
2. Go to https://render.com and create a Web Service.
3. Use this setting for **Start Command**:
   ```
   gunicorn app:app
   ```
4. Render will automatically install Flask and Gunicorn using `requirements.txt`.

5. After deployment, you'll get a public link like:
   ```
   https://your-app-name.onrender.com
   ```

## Using the App

- Go to the link
- Type:
  - Complex: `Ballylinny`
  - Room: `2`
- The app will show 2 example Dropbox photos

