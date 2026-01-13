%define oname Twiggy
%define	module	twiggy


Summary:	A Pythonic logger package

Name:		python-%{module}
Version:	0.5.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/t/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.org/projects/Twiggy
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(wheel)

%description
Twiggy is a logging package with a more Pythonic interface than
Python's own logger package.

%prep
%autosetup -n %{oname}-%{version} -p1
## Remove bundled egg-info
rm -rf %{oname}.egg-info

%build
%py_build
make -C doc html

%install
%py_install

%files
%doc README.rst  doc/_build/html
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%{version}*.*-info



