# Self-Destructing Emails
This repository contains a program that enables the sending of emails 
with a special feature: the email's content, such as a coupon or any other image, 
can only be viewed once.

## Motivations
Have you ever wondered if it's possible to send an email that can only be read once?
It seems challenging to achieve this with a regular text-based email, except by using AMP for emails.
However, since AMP for emails is not widely supported, it's not a practical option.

The next best solution is to send an HTML email with embedded content, such as an image,
that can only be viewed a single time. This approach is feasible because, in an email,
an image can be hosted externally, like this:

```html
<!-- The following image will be displayed in almost all email clients -->
<img src="https://external-domain.com/image" alt="an image"/>
```

By controlling the server hosting the image, it becomes possible to serve that specific 
image only once. As a result, the image will effectively "self-destruct" after it has been viewed!

## Usage
To use the program, follow these steps:

1. Install the required packages listed in the `requirements.txt` file.
2. Configure the SMTP server by providing the necessary details in the `main.py` file.
3. Adjust the `images_server_address` variable according to your setup. If running the program locally, you can set it to `http://localhost:8080`.
4. Run the command `python main.py` to execute the program.
5. Enter a valid email address when prompted, or type `stop` to terminate the program.

I have tested this program successfully with Mozilla Thunderbird. 
However, there might be issues with other email clients, particularly if you are hosting
the server locally without using HTTPS. If the server is configured correctly on a remote
machine with a valid SSL certificate, it should work fine.

## Notes
Please note that this code is experimental and lacks certain essential 
features such as sanity checks and input validation. Exercise caution while using it.