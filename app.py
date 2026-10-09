import streamlit as st

from analyzer import analyze_message
from risk_engine import generate_risk_report


# Explanation for each detected security indicator
INDICATOR_EXPLANATIONS = {

    "Urgency / time-pressure":
    "The message creates time pressure that may encourage the recipient to act quickly without verifying the request.",

    "urgent":
        "The message creates time pressure that may encourage the recipient to act without verifying the request.",

    "immediately":
        "The message uses immediate-action language, which is commonly seen in social engineering attempts.",

    "final warning":
        "The message creates pressure by presenting the request as a final warning.",

    "IP-based URL":
        "The URL uses a raw IP address instead of a domain name. This can be a suspicious characteristic.",

    "HTTP URL":
        "The URL uses HTTP instead of HTTPS, so the connection is not protected by TLS encryption.",

    "Possible brand impersonation":
        "A trusted brand name appears in a domain structure that may not belong to the legitimate brand.",

    "Password request":
        "The message asks for a password, which is sensitive authentication information.",

    "OTP request":
        "The message asks for a one-time password (OTP), which attackers may use to bypass authentication.",

    "Username request":
        "The message asks for a username or account identifier.",

    "Account blocking threat":
        "The message threatens to block the user's account, creating fear and pressure to act.",

    "Account suspension threat":
        "The message threatens to suspend the user's account.",

    "Possible lookalike domain":
        "The domain is highly similar to a known brand name but does not exactly match the legitimate brand domain.",

    "Threat / fear language":
        "The message uses threats or fear to pressure the recipient into taking action, such as claiming that an account will be suspended, blocked, or compromised.",

    "Credential request":
       "The message asks for sensitive authentication information, such as a username, password, or OTP, which could be used to gain unauthorized access.",
    
    "Unauthorized access":
        "The message claims that unauthorized access occurred, which can be used to create fear and urgency.",

}


# --------------------------------------------------
# Application Title
# --------------------------------------------------

st.title("🛡️ Phishing & Email Security Analyzer")

st.write(
    "Analyze messages and URLs for potential phishing indicators."
)


# --------------------------------------------------
# Message Input
# --------------------------------------------------

message = st.text_area(
    "Paste the email or message you want to analyze:",
    height=250
)


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🔍 Analyze Message"):

    if message.strip():

        # Analyze message
        analysis = analyze_message(message)

        # Generate risk report
        report = generate_risk_report(analysis)


        # --------------------------------------------------
        # Risk Assessment
        # --------------------------------------------------

        st.subheader("🛡️ Risk Assessment")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Risk Score",
                report["risk_score"]
            )

        with col2:

            risk_level = report["risk_level"]

            if risk_level == "HIGH":

                st.error(
                    f"🔴 {risk_level} RISK"
                )

            elif risk_level == "MEDIUM":

                st.warning(
                    f"🟡 {risk_level} RISK"
                )

            else:

                st.success(
                    f"🟢 {risk_level} RISK"
                )


        # --------------------------------------------------
        # Detected Indicators
        # --------------------------------------------------

        st.write("### Detected Indicators")

        if report["indicators"]:

            for indicator in report["indicators"]:

                st.write(
                    f"🔎 **{indicator}**"
                )

                explanation = INDICATOR_EXPLANATIONS.get(
                    indicator
                )

                if explanation:
                    st.caption(
                        explanation
                    )

        else:

            st.success(
                "No phishing indicators were detected."
            )


        # --------------------------------------------------
        # Recommendation
        # --------------------------------------------------

        st.subheader("💡 Recommendation")

        if risk_level == "HIGH":

            st.error(
                "Do not click the links or provide passwords, "
                "OTPs, or other sensitive information. "
                "Verify the request through an official channel."
            )

        elif risk_level == "MEDIUM":

            st.warning(
                "Exercise caution. Verify the sender and "
                "destination URL before taking any action."
            )

        else:

            st.success(
                "No major phishing indicators were detected. "
                "Continue to remain cautious with unexpected "
                "messages and links."
            )


        # --------------------------------------------------
        # URL Analysis
        # --------------------------------------------------

        st.subheader("🔗 URL Analysis")

        if analysis["url_analysis"]:

            for url_result in analysis["url_analysis"]:

                st.write("**URL:**")

                st.code(
                    url_result["url"]
                )


                if url_result["indicators"]:

                    st.write(
                        "**URL Indicators:**"
                    )

                    for indicator in url_result["indicators"]:

                        st.write(
                            f"🔎 **{indicator}**"
                        )

                        explanation = INDICATOR_EXPLANATIONS.get(
                            indicator
                        )

                        if explanation:

                            st.caption(
                                explanation
                            )

                else:

                    st.success(
                        "No URL-specific indicators detected."
                    )

        else:

            st.info(
                "No URLs were found in the message."
            )


    else:

        st.warning(
            "Please enter a message to analyze."
        )