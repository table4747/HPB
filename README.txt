# Holiday Photo App – Ballylinny Version

## How to Run

1. Make sure Python is installed (version 3.7 or newer).
2. Install Flask:
   ```
   pip install flask
   ```

3. Open terminal or command prompt and go to this folder:
   ```
   cd path_to_this_folder
   ```

4. Run the app:
   ```
   python app.py
   ```

5. In your browser, go to:
   ```
   http://127.0.0.1:5000
   ```

6. Type:
   - Complex: `Ballylinny`
   - Room: `2`

   You’ll see 2 sample photos displayed from Dropbox.

## Add More Photos

1. Upload a photo to Dropbox.
2. Change the end of the link from `dl=0` to `raw=1`
3. Add it to the `photos` table in `database.db` using a tool like DB Browser for SQLite or by editing the code.

