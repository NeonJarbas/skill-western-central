#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-western-central.jarbasai=skill_western_central:WesternCentralSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-western-central',
    version='0.0.1',
    description='ovos classic western western skill plugin',
    url='https://github.com/JarbasSkills/skill-western-central',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_western_central": ""},
    package_data={'skill_western_central': ['locale/*', 'ui/*']},
    packages=['skill_western_central'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
