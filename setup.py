from setuptools import setup, find_packages

version = '1.0'

setup(name='policy.intranetwb',
      version=version,
      description="Policy of intranet WB",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'cirb.zopemonitoring',
          # -*- Extra requirements: -*-
          'collective.ckeditor',
          'cirb.footersitemap',
          'collective.quickupload',
          'Products.PloneFormGen',
          'qi.portlet.TagClouds',
          'plonetheme.intranetwb',
          'collective.galleriffic',
          'collective.easyslider',
          'Solgema.fullcalendar',
          'collective.gallery',
          'quintagroup.analytics',
         # 'collective.recaptcha',
          'collective.anysurfer',
         # 'collective.portlet.videoanysurfer',
         # 'collective.videoanysurfer',
          'collective.linguafaq',
          'collective.js.galleriffic',
         #'webcouturier.dropdownmenu',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
