%define tarname Twiggy
%define	module	twiggy
%define	rel		1
%if %mdkversion < 201100
%else
%endif

Summary:	A Pythonic logger package

Name:		python-%{module}
Version:	0.5.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/T/Twiggy/Twiggy-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.org/projects/Twiggy
BuildArch:	noarch
BuildRequires:	python-sphinx
BuildRequires:	python-sphinxcontrib-googleanalytics

%description
Twiggy is a logging package with a more Pythonic interface than
Python's own logger package.

%prep
%setup -q -n %{tarname}-%{version}

%build
make -C doc html

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc LICENSE  doc/_build/html
%{py_puresitedir}/%{tarname}*
%{py_puresitedir}/%{module}*



