---
description: Configuring SSO documentation
title: Configuring SSO
---

# SAML in BloodHound

BloodHound supports SAML 2.0 for Single Sign-On to authenticate users to your local tenant environment. This walkthrough will be using [authentik](https://goauthentik.io/) as the chosen identity provider, as it is included in our `docker-compose.dev.yml` file to facilitate various authentication flows. This guide assumes you are setting up SSO for development of BloodHound Community Edition, however, there are elements that can be borrowed from this guide to configure any SAML identity provider in your deployed BloodHound instance.

1. First, run `just bh-sso` in the terminal in order to spin up the authentik docker services. Note: Initial bootstrapping of authentik may take some time.

   ```
   just bh-sso
   ```

2. Go to `http://authentik.localhost/if/flow/initial-setup/` to register an admin email and password for your authentik server. If you're already registered, sign in as usual instead:

   <img src="https://github.com/user-attachments/assets/4fab9177-e263-4efe-b8e1-8c177538b0a2" width="700"/>

3. Afterwards, click "Admin interface" on the top right:

   <img src="https://github.com/user-attachments/assets/27c625d8-5a86-456a-8c72-7dfbb3d9a744" width="1200"/>

4. Then navigate to the left side bar menu under "Applications" and click "Providers". You will first create a provider object by clicking on either of the blue "Create" buttons:

   <img src="https://github.com/user-attachments/assets/9b00cc5f-44e2-4f95-b708-2294c52a7b66" width="1200"/>

5. Choose the "SAML Provider" option and click "Next". You should see these options below:

   <img src="https://github.com/user-attachments/assets/028bb335-d7b1-4f2f-b784-eef4fe8585ff" width="800"/>

6. Make sure to fill out/choose these parameters below (the rest can be left alone), and click "Finish":
   ```
   Name: authentik
   Authentication flow: default-authentication-flow (Welcome to authentik!)
   Authorization flow: default-provider-authorization-explicit-consent (Authorize Application)
   ACS URL: http://bloodhound.localhost/api/v2/login/saml/authentik/acs 
   Issuer: authentik
   Service Provider Binding: Post 
   Signing Certificate: authentik Self-signed Certificate
   ```

   <img src="https://github.com/user-attachments/assets/46ca81b5-42b4-4f1f-9ce4-c859451a0b5e" width="800"/>
   <img src="https://github.com/user-attachments/assets/28c3d3b4-7042-4442-b12e-405de0dc6108" width="800"/>
   <img src="https://github.com/user-attachments/assets/a9879f6c-e63e-42ac-8910-78f2c185d978" width="1200"/>

7. Next, you will proceed to create an Application. Navigate to the left side bar menu under "Applications" and click "Applications". Click on either of the blue "Create" buttons to get started. You should see these options below:

   <img src="https://github.com/user-attachments/assets/aab81cdb-bc6b-431c-a78c-7c00e0a95100" width="800"/>

8. Make sure to fill out/choose these parameters below (the rest can be left alone), and click "Create":
   ```
   Name: bhce
   Slug: bhce
   Provider: authentik 
   Launch URL: http://bloodhound.localhost/ui/login
   Check mark toggle to: Open in new tab
   ```

   <img src="https://github.com/user-attachments/assets/c1787186-07f0-46b3-ac94-f6ef03b8934b" width="800"/>

9. Now that both the Provider and Application are created, you'll need to download the "Metadata" in the "Related objects" section of the page below:

   <img src="https://github.com/user-attachments/assets/4e486ae2-f0ce-4576-bf32-84fa1981dc3c" width="1200"/>

10. In order to leverage your SAML IDP you will need to provide BloodHound with a Service Provider (SP) certificate and key. To quickly generate a self-signed certificate and key you can run the following command:

    ```
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
    ```

11. Copy and paste the contents of your certificate WITHOUT the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines into the `"sp_cert"` field of your BloodHound configuration file (e.g. `build.config.json` for local dev):

    > Note: This command will strip the new lines and throw the contents of the file into your clipboard, making it a lot easier to paste everything all on one line.

    ```
    # For macos
    tr -d '\n' < /path/to/your/cert.pem | pbcopy
    ```

    <img src="https://github.com/user-attachments/assets/c6c35447-ce46-4f2d-a5e2-9c27cad773a8" width="1000"/>


12. Copy and paste the contents of your SP private key into the `"sp_key"` field of your BloodHound coniguration file. However, you need to include newline characters `\n` within the content. And ensure you retain the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` header and footer.

13. The last thing you need to do in authentik is create a new user (the one that will be logging into bhce via saml). Navigate to the left side bar menu under "Directory" and click "Users". Click on the blue "Create" button to get started. You should see these options below:

    <img src="https://github.com/user-attachments/assets/68446219-03cb-4091-ae0d-0c268a111f24" width="800"/>

14. Make sure to fill out/choose these parameters below (the rest can be left alone), and click "Create":

    ```
    Username: SomeUserName
    User type: Internal
    email: spam@example1.com
    ```
    <img src="https://github.com/user-attachments/assets/2b5c9f54-5153-4ff7-a26c-361d7216aa7b" width="800"/>

15. Afterwards, click on your newly created user and set the password:

    <img src="https://github.com/user-attachments/assets/d69a497d-8de1-44af-8708-5bf746cec0e5" width="800"/>

16. Now it's time to set up the SAML configuration on bhce. Click the gear icon on the top right of the page, and click "Administration". Then navigate to the left side menu under "Authentication" and click "SAML Configuration". Fill in the "SAML Provider Name" with "authentik" and choose the "Metadata" file you downloaded from authentik earlier and click "Submit":

    <img src="https://github.com/user-attachments/assets/5a895c5a-108f-4835-8c9d-81ac3f3531a7" width="1000"/>

    Notice that the ACS URL is the same as the ACS URL on authentik below:

    <img src="https://github.com/user-attachments/assets/dbc18d20-45f9-4f63-b244-5fd28aea9950" width="1000"/>
    <img src="https://github.com/user-attachments/assets/862aa9fd-dff5-45ce-83db-8d9af58c3ecb" width="1000"/>

17. Just as you created a new user within the authentik side, you must do the same on the bhce side. Navigate to the left side menu under "Users" and click "Manage Users". Make sure that the "Email Address" and "Principal Name" are the exact same ones you have in authentik. Then click "Save":

    Note: Make sure the admin and new user don't have the same email address
    <img src="https://github.com/user-attachments/assets/cb2f7c1b-5cc7-45cf-b820-c9aa52c3f2e6" width="1000"/>

18. Great! Now that everything is set on both ends, log out of bhce and try to login via sso. There should be a new button for it like below:

    <img src="https://github.com/user-attachments/assets/dcc223a7-d561-4974-b1c5-18dec1485496" width="850"/>

19. If you have multiple SSO providers, choose the newly created "authentik" SSO Provider and click "Continue":

    <img src="https://github.com/user-attachments/assets/cf90f02e-2f2c-4f86-b43c-927035fffb6d" width="850"/>

20. You should now be redirected to authentik, which will then ask for your credentials and consent to sign into bhce.

    <img src="https://github.com/user-attachments/assets/4697cef5-7df8-4ab9-b096-60f5680ff217" width="850"/>

21. And once you click "Continue", you will have successfully logged into bhce via SAML SSO!

# OIDC in BloodHound

BloodHound now supports OpenID Connect (OIDC) for Single Sign-On to authenticate users to your local tenant environment! This walkthrough will also be using [authentik](https://goauthentik.io/) as the chosen identity provider, as it is included in our docker-compose.dev.yml file to facilitate various authentication flows. This guide assumes you are setting up SSO for development of BloodHound Community Edition, however, there are elements that can be borrowed from this guide to configure any OIDC identity provider in your deployed BloodHound instance.

1. First, run `just bh-sso` in the terminal in order to spin up the authentik docker services. Note: Initial bootstrapping of authentik may take some time.

   ```
   just bh-sso
   ```

2. Go to `http://authentik.localhost/if/flow/initial-setup/` to register an admin email and password for your authentik server. If you're already registered, sign in as usual instead:

   <img src="https://github.com/user-attachments/assets/4fab9177-e263-4efe-b8e1-8c177538b0a2" width="700"/>

3. Afterwards, click "Admin interface" on the top right:

   <img src="https://github.com/user-attachments/assets/27c625d8-5a86-456a-8c72-7dfbb3d9a744" width="1200"/>

4. Then navigate to the left side bar menu under "Applications" and click "Providers". You will first create a provider object by clicking on either of the blue "Create" buttons:

   <img src="https://github.com/user-attachments/assets/9b00cc5f-44e2-4f95-b708-2294c52a7b66" width="1200"/>

5. Choose the "OAuth2/OpenID Provider" option and click "Next". You should see these options below:

   <img src="https://github.com/user-attachments/assets/bf7f405a-03c9-4ff2-91df-5111a3b46b80" width="800"/>

6. Make sure to fill out/choose these parameters below (the rest can be left alone), and click "Finish":
   ```
   Name: authentik-oidc (any alphanumeric name with spaces is supported)
   Authentication flow: default-authentication-flow (Welcome to authentik!)
   Authorization flow: default-provider-authorization-explicit-consent (Authorize Application)
   Client type: Public
   Redirect URIs/Origins(RegEx): http://bloodhound.localhost/api/v2/sso/authentik-oidc/callback
   ```

   <img src="https://github.com/user-attachments/assets/6ac73f78-4924-47f3-ace9-1040e03c2016" width="800"/>
   <img src="https://github.com/user-attachments/assets/2403441a-571a-4ca4-a650-a8c25da58456" width="800"/>
   <img src="https://github.com/user-attachments/assets/565b6bb4-a26d-4cdf-8d01-fe42be6cbc3c" width="1200"/>

7. Next, you will proceed to create an Application. Navigate to the left side bar menu under "Applications" and click "Applications". Click on either of the blue "Create" buttons to get started. You should see these options below:

   <img src="https://github.com/user-attachments/assets/aab81cdb-bc6b-431c-a78c-7c00e0a95100" width="800"/>

8. Make sure to fill out/choose these parameters below (the rest can be left alone), and click "Create":
   ```
   Name: bhce-authentik (any alphanumeric name with spaces is supported)
   Slug: bhce-oidc
   Provider: authentik-oidc
   Launch URL: http://bloodhound.localhost/ui/login
   Check mark toggle to: Open in new tab
   ```

   <img src="https://github.com/user-attachments/assets/6521eb9e-86d4-4a12-a190-767b55823319" width="800"/>
   <img src="https://github.com/user-attachments/assets/e678de5a-5a38-4473-8552-f8d125727431" width="800"/>

9. The last thing you need to do in authentik is create a new user (the one that will be logging into bhce via OIDC). Navigate to the left side bar menu under "Directory" and click "Users". Click on the blue "Create" button to get started. You should see these options below:

    <img src="https://github.com/user-attachments/assets/68446219-03cb-4091-ae0d-0c268a111f24" width="800"/>

10. Make sure to fill out/choose these parameters below (the rest can be left alone), and click "Create":

    ```
    Username: SomeUserName
    User type: Internal
    email: spam@example1.com
    ```
    <img src="https://github.com/user-attachments/assets/2b5c9f54-5153-4ff7-a26c-361d7216aa7b" width="800"/>

11. Afterwards, click on your newly created user and set the password:

    <img src="https://github.com/user-attachments/assets/d69a497d-8de1-44af-8708-5bf746cec0e5" width="800"/>

12. Now it's time to set up the OIDC configuration on bhce. Click the gear icon on the top right of the page, and click "Administration". Then navigate to the left side menu under "Authentication" and click "SSO Configuration". Fill in the "OIDC Provider Name" with "authentik oidc". The "Client ID" and "Issuer" contents must be copied and pasted from authentik. Once all that information is filled in, click "Submit":

    <img src="https://github.com/user-attachments/assets/9431d15c-6027-42b8-8345-3db45f89312c" width="1000"/>
    <img src="https://github.com/user-attachments/assets/bd617e76-3861-4bd8-816c-ebc18c63fb79" width="875"/>

    
13. Just as you created a new user within the authentik side, you must do the same on the bhce side. Navigate to the left side menu under "Users" and click "Manage Users". Make sure that the "Email Address" and "Principal Name" are the exact same ones you have in authentik. Then click "Save":

    Note: Make sure the admin and new user don't have the same email address
    <img src="https://github.com/user-attachments/assets/538c18fa-74a8-48b1-9202-9c588f8497a7" width="1000"/>

14. Great! Now that everything is set on both ends, log out of bhce and try to login via sso. There should be a new button for it like below:

    <img src="https://github.com/user-attachments/assets/dcc223a7-d561-4974-b1c5-18dec1485496" width="850"/>

15. If you multiple SSO Providers, choose the newly created "authentik oidc" SSO Provider and click "Continue":

    <img src="https://github.com/user-attachments/assets/99ff93bd-682a-49ec-b144-062fd1348476" width="850"/>

16. You should now be redirected to authentik, which will then ask for your credentials and consent to sign into bhce.

17. And once you click "Continue", you will have successfully logged into bhce via OIDC SSO!