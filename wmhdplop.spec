%define name	wmhdplop
%define summary Wmhdplop is yet another monitoring applet
%define version	0.9.9
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
URL:		http://hules.free.fr/wmhdplop
Group:		Monitoring
BuildRequires:	imlib2-devel
BuildRequires:	freetype-devel
BuildRequires:  gkrellm-devel
BuildRequires:	gtk+2-devel
Requires:	hddtemp
Requires:	fonts-ttf-vera

%description
Wmhdplop is yet another dockapp for WindowMaker, or any
windowmanager/desktop  environment that handles dockapps (KDE
has a dockbar extension, and gnome swallows). It monitors your
hard-drives by sending visual stimuli to your cortex  each time
your /dev/hdx writes or reads anything.  Try to launch openoffice
and enjoy the wmhdplop show! (loading these kitties in mozilla
also works).

Features:
* 0-portability, won't compile/run on anything without a recent kernel
* useless animation reflecting disc I/O.
* another useless animation reflecting swap activity.
* annoying blinking leds.
* a textual information of your harddrive throughput.
* display of the hd temperature if the hddtemp daemon is running.

%package -n gkrellm-plugins-%{name}
Summary: Wmhdplop plugin for gkrellm
Group: Monitoring
Requires: gkrellm

%description -n gkrellm-plugins-%{name}
Wmhdplop plugin for gkrellm

%prep
rm -rf $RPM_BUILD_ROOT
%setup -n %{name}-%{version}

%build
%configure
%make

%install
%makeinstall

# gkhdplop
install -d -m 755 %{buildroot}%{_libdir}/gkrellm2/plugins
install -m 644 gkhdplop.so %{buildroot}%{_libdir}/gkrellm2/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS INSTALL ChangeLog
%{_bindir}/%{name}

%files -n gkrellm-plugins-%{name}
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS INSTALL ChangeLog
%{_libdir}/gkrellm2/plugins/gkhdplop.so

