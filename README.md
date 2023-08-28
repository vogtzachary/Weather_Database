## Weather Database Builder/Grapher

### About the project:
This project is a Weather Database Builder and Grapher using noaa-sdk.

### Requirements:
<ul>
<li>Python 3 - <a href="https://www.python.org/downloads/">Python Downloads</a></li>
<li>noaa-sdk - <a href="https://pypi.org/project/noaa-sdk/"> PyPI Link</a></li>
<li>sqlite3 - <a href="https://pypi.org/project/SQLite3-0611/"> PyPI Link</a></li>
<li>pandas - <a href="https://pypi.org/project/pandas/"> PyPI Link</a></li>
<li>matplotlib - <a href="https://pypi.org/project/matplotlib/"> PyPI Link</a></li>
</ul>

### How to use:
##### BuildWeatherDb.py
<ol>
<li>Insert your zipcode in BuildWeatherDb.py.</li>
<li>Running this file will build a database in the current directory.</li>
</ol>

##### ExtractTempHumidity.py
<ol>
<li>Run this file to query weather.db and write csv's for weeks 1-2, and 3-4.</li>
</ol>

##### celsius_plot.py, fahrenheit_plot.py, humidity_plot.py
<ul>
<li>These files build various graphs/charts from formatdata1.csv and formatdata2.csv, created by ExtractTempHumidity.py</li>
</ul>

### License:

#### MIT License:
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Note from the Author:
Thanks for reading! - Zak