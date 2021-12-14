%global         pypi_name       stem
%global         pypi_version    1.8.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1
Summary:        Python controller library for Tor

License:        LGPL-3.0
URL:            https://stem.torproject.org/
Source0:        https://github.com/torproject/stem/archive/refs/tags/%{pypi_version}.tar.gz#/%{pypi_name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Stem is a Python controller library for Tor. With it you can use Tor's control
protocol to script against the Tor process, or build things such as Nyx.

Documentation and tutorials available at stem.torproject.org.


%package        -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description    -n python3-%{pypi_name}
Stem is a Python controller library for Tor. With it you can use Tor's control
protocol to script against the Tor process, or build things such as Nyx.

Documentation and tutorials available at stem.torproject.org.


%package        -n python-%{pypi_name}-doc
Summary:        %{pypi_name} documentation

%description    -n python-%{pypi_name}-doc
Documentation for %{pypi_name}


%prep
%autosetup -n %{pypi_name}-%{pypi_version}


%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/tor-prompt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info


%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
* Wed Sep 29 2021 herengui <herengui@uniontech.com> - 1.8.0-1
- Initial package.