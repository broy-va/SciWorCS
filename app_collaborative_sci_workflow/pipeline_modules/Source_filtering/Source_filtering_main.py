
import subprocess

pipe = subprocess.Popen(
    ["/bin/bash", "/home/ubuntu/Webpage/app_collaborative_sci_workflow/External_Libraries/NiCad-4.0/scripts/Filter",
     granularity, language,
     input_sourceCode, filters,
     filtered_sourceCode]).communicate()

