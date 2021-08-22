REASONS = {
        "AM": "A fundamental security product. Helps protecting the endpoints against malwares. In its basic form, doesn't require maintenance.",
        "EDR": "Endpoint Detection and Response (EDR) helps monitoring the security of the environment, as well as responding to security threats in real-time. EDR can help organization not only to detects threats, but also investigate attacks. EDR can also detect attacks that use LoLBins which challenges the traditional Anti malwares. Requires at least some maintenance by the security information team.",
        "SIEM": "Security information and event management (SIEM) enables collecting, processing and investigating security events. SIEM is an important component in the security stack of organization, especially larger ones. SIEM requires maintenance by the information security teams: Collecting logs in varied environment requires effort. Also, tracking and prioritize the security incidents requires a SOC team.",
        "CONTAINERS":"Container security products usually protect the container environment in various ways. For example: Ensure that the containers are compliant with security standards, helps detecting attacks in real-time and detect vulnerable applications. Container security product is important when the organization relies on containers and Kubernetes in their environment. Some products also protect Serverless applications which aren’t necessarily run on containers.",
        "IDENTITY":"Identity security products protect the identities in the organization. Especially in larger organizations, the identities are a key component of the overall organization security. Compromised identities are significant part of many attacks, especially targeted ones. Using compromised identities, attackers can move laterally in the organization. Such products detect malicious and suspicious identities behavior, which can help to mitigate such threats.",
        "DDOS": "DDOS protection is important when the organization has internet-facing services, especially in production environments.",
        "VUL_SCANNER": "Vulnerability scanners helps the organization to ensure that all the services are fully patched. In many attacks, application vulnerabilities are the initial access vector.",
        "WAF": "Web Application Firewall (WAF) is important part of the security stack. Almost every organization uses web applications (for example: web site). WAF can protect against large number of web attacks. For example: SQLi, CSRF, SRFF, XSS etc.",
        "FIREWALL": "Firewall is a key component of the organization security stack and protects from various networking-related attacks.",
        "SQL": "A dedicated database security product is important when the organization has an excessive usage of databases. Such products usually include threat detection, vulnerability management and auditing.",
        "STORAGE":"Storage security products protect storage services against data breach and unwanted data access. In can also help protecting against misconfigurations which might cause to a security threat.",
        "CSPM":"Cloud Security Posture Management (CSPM) aims to measure the security health of the cloud workload. It helps to detect and mitigate misconfigurations threats and help users to be security compliant. Usually, such products don’t require a lot of maintenance and set up efforts.",
        "CWPP":"Cloud Workload Protection Platform (CWPP) aims to protect cloud workloads against security attacks. Unlike CSPM, which detects mostly misconfigurations, CWPP can help detecting and mitigating compromised cloud resources. While the set-up process is usually relatively easy, investigating the security incidents requires security effort.",
        "IOT":"IoT security products are varied and can protect IoT devices in several levels: protecting the device itself, protecting the data pipeline and networking-level protection.",
        "SCADA": "Industrial Control Systems (ICS) security products can protect industrial system against cyber-attacks. Attacks that involve ICS were observed in the past and can cause a significant damage to the company, usually in its core business.",
        "APPLICATION_CONTROL": "Application Control tools are important when there’s a requirement to restrict the applications that run on the computers and servers in the organization. It is sometimes challenging to configure such tools in a way that won’t block necessary applications. Therefore, this product is recommended mostly to sensitive environments.",
        "DLP": "Data loss prevention software is useful when there’s a risk of data loss or breach. Such products important especially in sensitive environments."
    }

NAMES = {
        "AM": "Anti malware",
        "EDR": "EDR",
        "SIEM": "SIEM",
        "CONTAINERS":"Containers security",
        "IDENTITY": "Identity protection",
        "DDOS": "DDOS protection",
        "VUL_SCANNER": "Vulnerability scanner",
        "WAF": "WAF",
        "FIREWALL": "Firewall",
        "SQL": "SQL",
        "STORAGE":"Storage services protection",
        "CSPM": "CSPM",
        "CWPP": "CWPP",
        "IOT": "IoT protection",
        "SCADA": "SCADA\ICS protection",
        "APPLICATION_CONTROL": "Application Control tool",
        "DLP": "DLP"
    }
def prepare_output(products):
    output = ""
    for k in products:
        # Example: WAF: 33%
        first_line = "%s: %s%%\n" % (NAMES[k], products[k])
        second_line = REASONS[k] + "\n\n"

        output = output + first_line + second_line
    return output

    
