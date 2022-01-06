#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-backcall
Version  : 0.2.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/a2/40/764a663805d84deee23043e1426a9175567db89c8b3287b5c2ad9f71aa93/backcall-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a2/40/764a663805d84deee23043e1426a9175567db89c8b3287b5c2ad9f71aa93/backcall-0.2.0.tar.gz
Summary  : Specifications for callback functions passed in to an API
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-backcall-license = %{version}-%{release}
Requires: pypi-backcall-python = %{version}-%{release}
Requires: pypi-backcall-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
========
backcall
========
.. image:: https://travis-ci.org/takluyver/backcall.png?branch=master
:target: https://travis-ci.org/takluyver/backcall

%package license
Summary: license components for the pypi-backcall package.
Group: Default

%description license
license components for the pypi-backcall package.


%package python
Summary: python components for the pypi-backcall package.
Group: Default
Requires: pypi-backcall-python3 = %{version}-%{release}

%description python
python components for the pypi-backcall package.


%package python3
Summary: python3 components for the pypi-backcall package.
Group: Default
Requires: python3-core
Provides: pypi(backcall)

%description python3
python3 components for the pypi-backcall package.


%prep
%setup -q -n backcall-0.2.0
cd %{_builddir}/backcall-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641506782
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-backcall
cp %{_builddir}/backcall-0.2.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-backcall/ab5eb48d7d29fa62b23b1895d7e83f10144e54d7
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-backcall/ab5eb48d7d29fa62b23b1895d7e83f10144e54d7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
