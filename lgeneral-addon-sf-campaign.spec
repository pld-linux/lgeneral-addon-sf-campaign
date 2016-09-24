Summary:	LGeneral game - SF Campaign addon
Summary(pl.UTF-8):	Gra Linux General - dodatek SF Campaign
Name:		lgeneral-addon-sf-campaign
Version:	1.0.2
Release:	1
License:	unknown
Group:		Applications/Games
Source0:	http://lgames.sourceforge.net/LGeneral/addons/sf-campaign.zip
# Source0-md5:	9de66a38d695982eccdcf787dc1487bc
URL:		http://lgames.sourceforge.net/LGeneral/addons.php
Requires:	lgeneral
Requires:	lgeneral-data-pg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains small fictitious WW2 campaign featuring
4 scenarios and 2 extra scenarios from incomplete new campaign.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera małą, fikcyjną kampanię II WŚ, zawierającą 4
scenariusze oraz 2 dodatkowe scenariusze z nowej, niekompletnej
kampanii.

%prep
%setup -q -n sf-campaign

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -a campaigns gfx maps nations scenarios units $RPM_BUILD_ROOT%{_datadir}/lgeneral

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt todo.txt
%{_datadir}/lgeneral/campaigns/sf-campaign
%{_datadir}/lgeneral/gfx/flags/sf-campaign.bmp
%{_datadir}/lgeneral/gfx/units/sf-campaign.bmp
%{_datadir}/lgeneral/maps/sf-campaign
%{_datadir}/lgeneral/maps/sf-campaign.tdb
%{_datadir}/lgeneral/nations/sf-campaign.ndb
%{_datadir}/lgeneral/scenarios/lesserscale
%{_datadir}/lgeneral/scenarios/sf-campaign
%{_datadir}/lgeneral/units/sf-campaign.udb
