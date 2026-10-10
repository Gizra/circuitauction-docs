# Logging in with an Authenticator App

From version 3.5 the backoffice can protect staff accounts with **two-factor authentication**: besides your username and password, every login asks for a six-digit code from an authenticator app on your phone, such as Authy, Google Authenticator or Microsoft Authenticator.

<video class="release-video" controls preload="metadata" playsinline src="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-authenticator-setup/final.mp4">Your browser does not support the video tag. <a href="https://circuit-kubernetes.s3.eu-central-1.amazonaws.com/openmontage/tutorials/release-3.5-authenticator-setup/final.mp4">Download the video</a>.</video>

## First login: set up the app

The first time you log in after the feature is switched on for your account, the backoffice takes you to a one-time **Authenticator app** setup page before anything else. You cannot open other pages until it is done.

![The authenticator app setup page: QR code, manual key and the first-code field](assets/screenshots/authenticator-setup-page.png)

1. **Install an authenticator app** on your phone (Authy, Google Authenticator and Microsoft Authenticator all work).
2. **Scan the QR code** shown on the page with the app. If you cannot scan it, add the account manually in the app and type the **manual key** shown under the QR code.
3. The app now shows a **six-digit code** that changes every 30 seconds. Type the current code in the **Code** field and click **Activate**.

If the code is rejected, wait for the next one in the app and try again. The clock on your phone must be correct for the codes to match.

After activation you land on the dashboard as usual.

## Every following login

Enter your username and password as before. A **Code** field appears under the password: type the current code from your app and click **Log in**.

If you sign in with Google, the same code is asked for after Google confirms your account.

## Lost or replaced phone

The codes live only in the app on your phone. If you lose it or move to a new phone, ask an administrator to **reset the authenticator app** from your user account (the *Reset authenticator app* option on the user form). Your next login then shows the setup page again, so you can enrol the new phone.

## For administrators

- The feature is switched on site-wide in the server settings (*Require an authenticator app for staff logins*). It is off by default, so an upgrade never locks anyone out.
- Independently of the site-wide setting, a user account can be marked **Always require an authenticator app for this account**.
- The user list shows an **Authenticator** column with each account's status, and the user form shows whether the app is activated and lets you reset it.
- Customer (bidder) accounts on the website are not affected.

See also [Logging into the System](logging-into-the-system.md).
