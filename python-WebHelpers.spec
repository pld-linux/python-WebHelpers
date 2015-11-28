%define		fname		WebHelpers
Summary:	Web Helpers
Summary(pl.UTF-8):	Web Helpers - funkcje pomocniczne dla aplikacji WWW
Name:		python-%{fname}
Version:	0.6.4
Release:	3
License:	Pylons
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/W/WebHelpers/%{fname}-%{version}.tar.gz
# Source0-md5:	d11ed399068aac9368281497d40a4436
URL:		http://pylonshq.com/WebHelpers/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-setuptools >= 0.6-0.c7.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier.

One of the sub-sections of Web Helpers contains a full port of the
template helpers that are provided by Ruby on Rails with slight
adaptations on occasion to accomodate for Python.

%description -l pl.UTF-8
Web Helpers to biblioteka funkcji pomocniczych mających ułatwić
tworzenie szablonów w aplikacjach WWW.

Jedna z części Web Helpers zawiera pełny port funkcji pomocniczych dla
szablonów dostarcznych przez Ruby on Rails z nieznacznymi adaptacjami
pod kątem Pythona.

%prep
%setup -qn %{fname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/webhelpers
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
