%define tarname Twiggy
%define	module	twiggy
%define name	python-%{module}
%define version	0.4.4
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	A Pythonic logger package
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/T/%{tarname}/%{tarname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.google.com/p/python-twiggy/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel, python-sphinx
BuildRequires:	python-sphinxcontrib-googleanalytics

%description
Twiggy is a logging package with a more Pythonic interface than
Python's own logger package.

%prep
%setup -q -n %{tarname}-%{version}

%build
make -C doc html

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README doc/_build/html
%py_sitedir/%{tarname}*
%py_sitedir/%{module}*
