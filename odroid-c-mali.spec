%global commit cdf9ddb1cb2090f2c25dc4b4cca5e0d73d8db17c

Name:           odroid-c-mali
Version:        2016.09.12
Release:        2%{?dist}
Summary:        Mali GL Binaries for ODROID-C

Group:          System Environment/Libraries
License:        Proprietary
URL:            https://github.com/mdrjr/c1_mali_libs
Source0:        https://github.com/mdrjr/c1_mali_libs/archive/%{commit}/c1_mali_libs-%{commit}.tar.gz

%package fb
Summary:        Mali GL Binaries for ODROID-C (Frame Buffer)
Conflicts:      %{name}-x11
Provides:       libEGL.so
Provides:       libEGL.so.1
Provides:       libGLESv1_CM.so
Provides:       libGLESv1_CM.so.1
Provides:       libGLESv2.so
Provides:       libGLESv2.so.2

%package x11
Summary:        Mali GL Binaries for ODROID-C (X11)
Conflicts:      %{name}-fb
Provides:       libEGL.so
Provides:       libEGL.so.1
Provides:       libGLESv1_CM.so
Provides:       libGLESv1_CM.so.1
Provides:       libGLESv2.so
Provides:       libGLESv2.so.2

%package ump
Summary:        Mali GL Binaries for ODROID-C (UMP)

%package ump-devel
Summary:        Mali GL Binaries for ODROID-C (UMP Headers)
Requires:       %{name}-ump%{?_isa} = %{version}-%{release}

%description
Mali GL Binaries for ODROID-C based on r6p2-01rel0

%description fb
Mali GL Binaries for ODROID-C (Frame Buffer) based on r6p2-01rel0

%description x11
Mali GL Binaries for ODROID-C (X11) based on r6p2-01rel0

%description ump
Mali GL Binaries for ODROID-C (UMP) based on r6p2-01rel0

%description ump-devel
Mali GL Binaries for ODROID-C (UMP Headers) based on r6p2-01rel0

%prep
%setup -qn c1_mali_libs-%{commit}

chmod 644 *.md

# The LICENSE.md file is a symlink - it needs to be resolved for %%license to work
cp --remove-destination `readlink LICENSE.md` LICENSE.md

%build

%install
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d/
install -d %{buildroot}%{_includedir}/ump/
install -d %{buildroot}%{_includedir}/umplock/

install -m0755 -p -D fbdev/mali_libs/libMali.so %{buildroot}%{_libdir}/odroid-c-mali-fb/libMali.so
install -m0755 -p -D x11/mali_libs/libMali.so %{buildroot}%{_libdir}/odroid-c-mali-x11/libMali.so
install -m0755 -p -D x11/mali_libs/libUMP.so %{buildroot}%{_libdir}/libUMP.so
install -m0644 -p x11/mali_headers/ump/* %{buildroot}%{_includedir}/ump/
install -m0644 -p x11/mali_headers/umplock/* %{buildroot}%{_includedir}/umplock/

echo "%{_libdir}/odroid-c-mali-fb" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/odroid-c-mali-fb.conf
echo "%{_libdir}/odroid-c-mali-x11" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/odroid-c-mali-x11.conf

ln -s libMali.so %{buildroot}%{_libdir}/odroid-c-mali-fb/libEGL.so.1.0.0
ln -s libEGL.so.1.0.0 %{buildroot}%{_libdir}/odroid-c-mali-fb/libEGL.so
ln -s libEGL.so.1.0.0 %{buildroot}%{_libdir}/odroid-c-mali-fb/libEGL.so.1
ln -s libMali.so %{buildroot}%{_libdir}/odroid-c-mali-fb/libGLESv2.so.2.0.0
ln -s libGLESv2.so.2.0.0 %{buildroot}%{_libdir}/odroid-c-mali-fb/libGLESv2.so
ln -s libGLESv2.so.2.0.0 %{buildroot}%{_libdir}/odroid-c-mali-fb/libGLESv2.so.2
ln -s libMali.so %{buildroot}%{_libdir}/odroid-c-mali-fb/libGLESv1_CM.so.1.1
ln -s libGLESv1_CM.so.1.1 %{buildroot}%{_libdir}/odroid-c-mali-fb/libGLESv1_CM.so
ln -s libGLESv1_CM.so.1.1 %{buildroot}%{_libdir}/odroid-c-mali-fb/libGLESv1_CM.so.1

ln -s libMali.so %{buildroot}%{_libdir}/odroid-c-mali-x11/libEGL.so.1.0.0
ln -s libEGL.so.1.0.0 %{buildroot}%{_libdir}/odroid-c-mali-x11/libEGL.so
ln -s libEGL.so.1.0.0 %{buildroot}%{_libdir}/odroid-c-mali-x11/libEGL.so.1
ln -s libMali.so %{buildroot}%{_libdir}/odroid-c-mali-x11/libGLESv2.so.2.0.0
ln -s libGLESv2.so.2.0.0 %{buildroot}%{_libdir}/odroid-c-mali-x11/libGLESv2.so
ln -s libGLESv2.so.2.0.0 %{buildroot}%{_libdir}/odroid-c-mali-x11/libGLESv2.so.2
ln -s libMali.so %{buildroot}%{_libdir}/odroid-c-mali-x11/libGLESv1_CM.so.1.1
ln -s libGLESv1_CM.so.1.1 %{buildroot}%{_libdir}/odroid-c-mali-x11/libGLESv1_CM.so
ln -s libGLESv1_CM.so.1.1 %{buildroot}%{_libdir}/odroid-c-mali-x11/libGLESv1_CM.so.1

%post fb -p /sbin/ldconfig

%post x11 -p /sbin/ldconfig

%post ump -p /sbin/ldconfig

%postun fb -p /sbin/ldconfig

%postun x11 -p /sbin/ldconfig

%postun ump -p /sbin/ldconfig

%files fb
%doc README.md
%license LICENSE.md
%{_libdir}/odroid-c-mali-fb/
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/odroid-c-mali-fb.conf

%files x11
%doc README.md
%license LICENSE.md
%{_libdir}/odroid-c-mali-x11/
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/odroid-c-mali-x11.conf

%files ump
%doc README.md
%license LICENSE.md
%{_libdir}/libUMP.so

%files ump-devel
%{_includedir}/ump/
%{_includedir}/umplock/

%changelog
* Wed Oct 19 2016 Scott K Logan <logans@cottsay.net> - 2016.09.12-2
- Add LICENSE.md and README.md

* Fri Oct 14 2016 Scott K Logan <logans@cottsay.net> - 2016.09.12-1
- Update to latest source

* Wed Dec 02 2015 Scott K Logan <logans@cottsay.net> - 2015.10.15-1
- Initial package
