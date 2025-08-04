print(""" Cons / Challenges
Legal Validity Issue

Courts may not accept AI-generated partitions as legally binding unless approved by licensed surveyors or revenue officers.

You might need integration with certified architects or surveyors.

Complex Algorithm Requirement

Designing an AI to calculate fair and practical partitions is technically challenging:

Must handle irregular land shapes

Consider legal easements & road access

Handle multi-floor or multi-use properties

Data Privacy & Security

Property blueprints are sensitive.

Need strong data protection to gain user trust.

Initial Adoption Barrier

Lawyers and clients may hesitate to trust an AI-generated partition initially.

Education and demo cases will be needed.

Regulatory Compliance

Need to ensure your website does not violate surveying or property registration laws in India.

Final partition must still be validated by government authorities. """)


import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty('rate', 150)     # Speed of speech (default ~200)
engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

# Text to speak
text = "Hello Yaseen! Welcome to Python text to speech."

# Speak the text
engine.say(text)

# Run and wait for the speaking to finish
engine.runAndWait()
