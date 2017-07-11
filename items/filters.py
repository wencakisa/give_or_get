from rest_framework import filters


class IsItemOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)


class IsActiveItemFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_active = request.query_params.get('is_active', 'true')
        is_active = is_active.lower() == 'true'

        return queryset.filter(item__is_active=is_active)


class DealTypeFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user

        deal_type = view.kwargs.get('deal_type')
        if deal_type == 'personal':
            return queryset.filter(item__owner=user)
        elif deal_type == 'following':
            return queryset.filter(buyer=user)
