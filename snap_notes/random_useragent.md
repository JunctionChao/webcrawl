### random useragent

[random-user-agent · PyPI](https://pypi.org/project/random-user-agent/)

[random-user-agent github](https://github.com/Luqman-Ud-Din/random_user_agent)

```python
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# Get list of user agents.
user_agents = user_agent_rotator.get_user_agents()

# Get Random User Agent String.
user_agent = user_agent_rotator.get_random_user_agent()
```

- #### pc useragent

  ```python
  from random_user_agent.user_agent import UserAgent
  from random_user_agent.params import SoftwareName, OperatingSystem
  
  pc_sn = [SoftwareName.CHROME.value, SoftwareName.OPERA.value, SoftwareName.FIREFOX.value, SoftwareName.SAFARI.value]
  ops = [OperatingSystem.WINDOWS.value, OperatingSystem.MAC.value, OperatingSystem.LINUX.value]
  user_agent_rotator = UserAgent(software_names=pc_sn, operating_systems=ops, limit=100)
  
  pc_ua = user_agent_rotator.get_random_user_agent()
  ```

- #### mobile useragent

  ```python
  from random_user_agent.user_agent import UserAgent
  from random_user_agent.params import SoftwareName, OperatingSystem
  
  mobile_sn = [SoftwareName.CHROME.value, SoftwareName.OPERA.value, SoftwareName.FIREFOX.value, SoftwareName.SAFARI.value]
  ops = [OperatingSystem.ANDROID.value, OperatingSystem.IOS.value]
  user_agent_rotator = UserAgent(software_names=mobile_sn, operating_systems=ops, limit=100)
  
  mobile_ua = user_agent_rotator.get_random_user_agent()
  ```

  
