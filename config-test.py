import yaml

config = yaml.safe_load(open("config.yml"))

print(config['KVM_PW'])