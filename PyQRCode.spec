#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyQRCode
Version  : 1.2.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/37/61/f07226075c347897937d4086ef8e55f0a62ae535e28069884ac68d979316/PyQRCode-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/37/61/f07226075c347897937d4086ef8e55f0a62ae535e28069884ac68d979316/PyQRCode-1.2.1.tar.gz
Summary  : A QR code generator written purely in Python with SVG, EPS, PNG and terminal output.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: PyQRCode-python = %{version}-%{release}
Requires: PyQRCode-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
PyQRCode
        ========

%package python
Summary: python components for the PyQRCode package.
Group: Default
Requires: PyQRCode-python3 = %{version}-%{release}
Provides: pyqrcode-python

%description python
python components for the PyQRCode package.


%package python3
Summary: python3 components for the PyQRCode package.
Group: Default
Requires: python3-core
Provides: pypi(pyqrcode)

%description python3
python3 components for the PyQRCode package.


%prep
%setup -q -n PyQRCode-1.2.1
cd %{_builddir}/PyQRCode-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603401194
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
