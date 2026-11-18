"""Builds the static site pages (shared header/footer). Run: python build_site.py"""
import os, shutil
D = os.path.dirname(os.path.abspath(__file__))
shutil.copy(r'D:\Agents\venture2\site\style.css', os.path.join(D, 'style.css'))
with open(os.path.join(D, 'style.css'), 'a', encoding='utf8') as f:
    f.write('\n.steps{line-height:1.7;padding-left:1.2em}\n.steps li{margin:4px 0}\n')

HDR = '<header class="wrap top"><a class="brand" href="./">Scheduled Sheet Reports</a><nav><a href="./#features">Features</a><a href="./#pricing">Pricing</a><a href="support.html">Support</a></nav></header>'
FTR = '<footer class="wrap foot"><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms of service</a><a href="support.html">Support</a><span>&copy; 2026 Myzles</span><span class="small">Google Sheets, Gmail and Google Workspace are trademarks of Google LLC.</span></footer>'
YEARLY = 'https://buy.polar.sh/polar_cl_2FCOJj0OA82YPhj2kNXq5B5Lyd6tLaUT3I5VF2hyjky'
MONTHLY = 'https://buy.polar.sh/polar_cl_g5BD1GO6BYs2bRUYo3kjSf56NTwhfmg9c0Htf2Jf3jh'
MAIL = '<a href="mailto:swagstudios.helpdesk@outlook.com">swagstudios.helpdesk@outlook.com</a>'


def page(name, title, body, desc=''):
    meta = f'<meta name="description" content="{desc}">\n' if desc else ''
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{meta}<link rel="stylesheet" href="style.css">
</head>
<body>
{HDR}
{body}
{FTR}
</body>
</html>
'''
    import re
    # Google asks for a trademark mark after each Google product name (the Dedupe & Match rejection)
    for prod in ('Google Apps Script', 'Google Sheets', 'Google Workspace', 'Gmail'):
        html = re.sub(re.escape(prod) + '(?!™|&trade;)', prod + '™', html)
    with open(os.path.join(D, name), 'w', encoding='utf8') as f:
        f.write(html)


page('index.html', 'Scheduled Sheet Reports for Google Sheets', f'''
<section class="wrap hero">
  <h1>Email your Google Sheets reports on a schedule. Stop them with one click.</h1>
  <p class="lead">Pick a range, a tab or the whole file. Choose PDF, Excel, CSV or a table right in the email. Pick the day and hour. It goes out from your own Gmail, and you can always see when it last ran.</p>
  <p><!-- LAUNCH-INSTALL: Marketplace install button goes here after approval (Google: no coming-soon text before OAuth review) --></p>
  <p class="small">Free for one schedule. No account to create.</p>
</section>

<section id="features" class="wrap grid">
  <div><h3>Every schedule in one list</h3><p>See every report you have set up, in every spreadsheet, from any spreadsheet. Pause or delete one and it stops right away. "Pause all" stops everything at once.</p></div>
  <div><h3>You can tell it's working</h3><p>Each schedule shows when it last ran, what it sent, when it runs next and a short history. If Google hasn't checked a file for a while, the sidebar says so and fixes it in one click.</p></div>
  <div><h3>When something breaks, you hear about it</h3><p>Google hiccups are retried on their own. If a report still can't go out (a deleted tab, a typo in an address), you get one email saying what happened and how to fix it. Not one a day.</p></div>
  <div><h3>The format your team wants</h3><p>A PDF of exactly the range or tab you picked. Excel or CSV of exactly the range you picked. Or a formatted table in the email body, colors and bold included.</p></div>
  <div><h3>Send only when it matters</h3><p>Hold a report back when the range is empty, when nothing changed since last time, or until a cell says TRUE. Put live numbers in the subject with <code>{{{{Summary!B2}}}}</code>.</p></div>
  <div><h3>Your data stays in Google</h3><p>Runs on Google's servers under your account and your Gmail sending limit. Nothing is copied to our servers, because we don't have any.</p></div>
</section>

<section class="wrap">
  <h2>How it works</h2>
  <ol class="steps">
    <li>Open your spreadsheet, then Extensions, Scheduled Sheet Reports, New schedule.</li>
    <li>Choose what to send and the format, add the email addresses, pick when.</li>
    <li>Press "Send me a test" to see exactly what arrives. Then Save.</li>
  </ol>
  <p class="small">Reports go out during the hour you choose (Google runs add-on timers once an hour), in your spreadsheet's time zone. Daylight saving changes never move them.</p>
</section>

<section id="pricing" class="wrap">
  <h2>Pricing</h2>
  <div class="plans">
    <div class="plan"><h3>Free</h3><p class="price">$0</p><ul><li>1 running schedule</li><li>Every format and condition</li><li>Daily, weekly and monthly</li></ul></div>
    <div class="plan best"><span class="tag">Best value</span><h3>Pro yearly</h3><p class="price">$60<span>/year</span></p><ul><li>Unlimited schedules in every spreadsheet</li><li>Reports every 1 to 12 hours</li><li>No "Sent with" line in your emails</li><li>2 months free vs monthly</li></ul><a class="btn" href="{YEARLY}">Get Pro yearly</a></div>
    <div class="plan"><h3>Pro monthly</h3><p class="price">$6<span>/month</span></p><ul><li>Everything in Pro</li><li>Cancel any time</li></ul><a class="btn ghost" href="{MONTHLY}">Get Pro monthly</a></div>
  </div>
  <p class="small">Your license key arrives by email right after checkout. Paste it at the bottom of the sidebar. One key works in every spreadsheet and Google account you use. Payments are handled by Polar, which also takes care of sales tax and VAT. If Pro ends, nothing is deleted: extra schedules pause until you renew.</p>
</section>
''', 'Email a Google Sheets range, tab or whole file on a schedule as PDF, Excel, CSV or a table in the email. One list of every schedule, and Pause works instantly.')

exec(open(os.path.join(D,'privacy_section.py'),encoding='utf8').read())
page('privacy.html', 'Privacy Policy - Scheduled Sheet Reports', PRIVACY.replace('{MAIL}', MAIL))

page('terms.html', 'Terms of Service - Scheduled Sheet Reports', f'''<main class="wrap doc">
<h1>Terms of Service</h1>
<p class="small">Last updated: November 17, 2026</p>
<p>These terms cover your use of the Scheduled Sheet Reports add-on for Google Sheets, made by Myzles ("we"). By installing or using it you agree to them.</p>
<h2>The service</h2>
<p>Scheduled Sheet Reports emails parts of your Google Sheets on a schedule you set. The free version runs one schedule at a time. A Pro subscription allows unlimited schedules and reports every few hours.</p>
<h2>Subscriptions and payment</h2>
<ul>
<li>Pro is sold as a monthly or yearly subscription through Polar, our merchant of record. Polar handles billing, receipts, sales tax and VAT.</li>
<li>Subscriptions renew automatically until cancelled. You can cancel at any time from the link in your receipt email; Pro stays active until the end of the period you paid for.</li>
<li>If Pro does not work for you, reply to your receipt within 7 days of a payment for a full refund.</li>
<li>A license key is for one person. You can use it in any spreadsheet and any Google account you personally use.</li>
</ul>
<h2>Email you send</h2>
<p>Reports are sent from your own Google account, to recipients you choose, and count against Google's daily sending limit for your account. You are responsible for having permission to email your recipients and for what your reports contain. Do not use the add-on to send spam.</p>
<h2>Delivery</h2>
<p>Reports depend on Google's timers, export and email services. We retry temporary failures and tell you when a report could not be sent, but we cannot guarantee that every report arrives, or arrives at a specific minute.</p>
<h2>Your data</h2>
<p>Your spreadsheets stay yours. The add-on processes them inside Google and does not send their contents to us. See the <a href="privacy.html">Privacy Policy</a>.</p>
<h2>Acceptable use</h2>
<p>Do not resell or share license keys, try to bypass the license check, or use the add-on to break the law.</p>
<h2>No warranty</h2>
<p>The add-on is provided "as is". To the extent the law allows, our total liability is limited to the amount you paid us in the 12 months before a claim.</p>
<h2>Changes and termination</h2>
<p>We may update the add-on and these terms. If a change materially affects paid subscribers, we will email them before it takes effect. You can stop using the add-on at any time by uninstalling it.</p>
<h2>Contact</h2>
<p>{MAIL}</p>
</main>''')

page('support.html', 'Support - Scheduled Sheet Reports', f'''<main class="wrap doc">
<h1>Support</h1>
<p>Email {MAIL}. A person reads every message and replies within one business day.</p>
<h2>How do I stop a report?</h2>
<p>Open any spreadsheet, then Extensions, Scheduled Sheet Reports, Manage schedules. Every schedule you own is listed, including ones in other files. Press Pause or Delete; it takes effect immediately. To stop everything, use Extensions, Scheduled Sheet Reports, Pause all my schedules. Uninstalling the add-on also stops all of them.</p>
<h2>A report didn't arrive</h2>
<ul>
<li>Open Manage schedules and look at the schedule's status and History. It says what happened at each run.</li>
<li>Reports go out during the hour you chose, not on the minute. Times use the spreadsheet's time zone (File, Settings).</li>
<li>Check the recipient's spam folder, especially for the first report.</li>
<li>If the sidebar says Google hasn't checked the file for a while, press "Repair the timer".</li>
<li>Google limits how many people you can email per day: about 100 for free Gmail accounts and 1,500 for Workspace. Each recipient counts. A report held by the limit goes out when it resets, the same day.</li>
</ul>
<h2>The PDF looks wrong</h2>
<p>The PDF follows the sheet's own column widths and formatting. Narrow the columns or pick a smaller range, then press "Send me a test" to compare. Hidden rows and columns are left out of the Excel, CSV and email table.</p>
<h2>Which formats can I send?</h2>
<p>PDF, Excel (.xlsx), CSV and a table in the email body, in any combination. For the whole file, Excel is Google's full export with every tab, and CSV sends one file per tab.</p>
<h2>Can I put numbers from the sheet in the subject?</h2>
<p>Yes. Use {{{{B2}}}} for a cell on the same tab or {{{{Summary!B2}}}} for another tab. Also {{{{date}}}}, {{{{time}}}}, {{{{day}}}}, {{{{month}}}}, {{{{file}}}} and {{{{tab}}}}.</p>
<h2>Licenses and billing</h2>
<p>Your key is in the email Polar sent after checkout. Paste it at the bottom of the sidebar. To cancel, use the link in that email. If Pro ends, nothing is deleted: your oldest daily, weekly or monthly schedule keeps running and the rest pause until you renew. Refunds: reply to your receipt within 7 days for a full refund, no questions asked. Buying for a team of 3 or more? Reply to any receipt and ask for a team price.</p>
</main>''')
print('built', os.listdir(D))
