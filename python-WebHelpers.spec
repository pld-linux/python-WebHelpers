%define 	module	        webhelpers
%define     fname           WebHelpers
%define     python_version  2.5
Summary:	Web Helpers
Name:		python-%{fname}
Version:	0.2.2
Release:	0.1
License:	Pylons
Group:		Libraries/Python
Source0:    http://cheeseshop.python.org/packages/source/W/%{fname}/%{fname}-%{version}.tar.gz
# Source0-md5:	c0d82bbf6126a641e01c73a3696ddd2d
URL:		http://pylonshq.com/WebHelpers/
BuildRequires:  python-setuptools
Requires:	python >= %{python_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier.

One of the sub-sections of Web Helpers contains a full port of the template
helpers that are provided by Ruby on Rails with slight adaptations on occasion
to accomodate for Python.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{fname}-%{version}-py%{python_version}.egg-info
